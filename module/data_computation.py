import logging


def hex_to_bin(hex_string):
    try:
        binary_string = bin(int(hex_string, 16))[2:]
        return binary_string
    except ValueError:
        logging.error("Invalid hexadecimal input.")

def split_string(input_string):

    padded_input = input_string.zfill(64)

    types = padded_input[60:64]
    time = padded_input[20:60]
    state = padded_input[16:20]
    state_of_charge = padded_input[8:16]
    temperature = padded_input[0:8]
    splited_list = [types, time, state, state_of_charge, temperature]
    return splited_list

def get_status_string(status_code):
    if 0 <= status_code <= 8:
        status_mapping = {
            0: "power off",
            1: "power on",
            2: "discharge",
            3: "charge",
            4: "charge complete",
            5: "host mode",
            6: "shutdown",
            7: "error",
            8: "undefined"
        }

        return status_mapping.get(status_code)
    else:
        logging.error(f"Invalid status code as not between 0-8 {status_code}",)


def bin_to_dec(bin_string):
    try:
        binary_string = int(bin_string, 2)
        return binary_string
    except ValueError:
        logging.error("Invalid binary input")


def compute_data(lst):

    lst[0] = bin_to_dec(lst[0])
    lst[1] = bin_to_dec(lst[1])
    lst[2] = get_status_string(bin_to_dec(lst[2]))
    lst[3] = (bin_to_dec(lst[3])) / 2
    lst[4] = (bin_to_dec(lst[4]) / 2) - 20
    return lst
