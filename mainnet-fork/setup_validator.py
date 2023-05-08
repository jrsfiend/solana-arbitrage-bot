"""setup validator"""
import json
import os

local_validator_command = "solana-test-validator -r --account-dir accounts/"

with open("programs.json", 'r', encoding='utf-8') as f:
    programs = json.load(f)

for prog in programs:
    command = "solana program dump -u m {prog} programs/{prog}.so".format(prog=prog)
    print(f"CMD: {command}")

    # Create folder if not exists "programs"
    os.system(command)
    
    local_validator_command += " --bpf-program {prog} programs/{prog}.so ".format(prog=prog)

with open('start_localnet.sh', 'w', encoding='utf-8') as f:
    f.write(local_validator_command)
