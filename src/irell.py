import lldb
import argparse

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand("command script add -f irell.bb bb -h 'set breakpoint at address considering ASLR'")


def bb(debugger, command, result, internal_dict):
    debugger = lldb.debugger
    target = debugger.GetSelectedTarget()
    loaded_address = target.GetModuleAtIndex(0).GetSectionAtIndex(1).GetLoadAddress(target)
    aslr_slide = loaded_address - 0x100000000


    parser = argparse.ArgumentParser(prog="")
    parser.add_argument("address")
    args = parser.parse_args(command.split())
    lldb.debugger.HandleCommand (f"br set -a {int(args.address, 16)+aslr_slide}")