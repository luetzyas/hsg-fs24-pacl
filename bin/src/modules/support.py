# imports
import inspect as ip

# This function is to handle the tracebility text in the console
def tracebility_handling_start(trace: bool) -> None:
    # inform tracebility in console log
    trace_status_txt = 'deactivated'

    if trace: 
        trace_status_txt = 'activated'
    print(f"--- Tracebility is {trace_status_txt} ---")

# This function checks and prints the message
def traceability_handling_prints(trace, text):
    if trace:
        print(f"--- Def:{text} ---")
