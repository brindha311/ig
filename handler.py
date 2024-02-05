import logging
import os
from module import file_processing, data_computation

# Configure the logging settings
logging.basicConfig(filename='logfile.log', level=logging.DEBUG)

def handler():
    # Get the current script's directory
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Create the path to the file in the 'src_data' folder
    src_path = os.path.join(script_dir, 'src_data')
    # path for the files after processed
    processed_path = os.path.join(script_dir, 'processed_data')
    try:
        files = [f for f in os.listdir(src_path) if f.lower().endswith('.json')]
        # Iterate over each CSV file and read into the DataFrame
        for file_name in files:
            json_file_path = os.path.join(src_path, file_name)
            dic = file_processing.read_json_file(json_file_path)
            dic["binary_output"] = data_computation.hex_to_bin(dic["payload"])
            compute = data_computation.compute_data(
                                data_computation.split_string(dic["binary_output"]))
            compute.pop(0)
            compute.insert(0, dic['device'])

            keys = ["device", "time", "state", "state_of_charge", "temperature"]

            final = dict(zip(keys, compute))
            end_name_path = json_file_path.split("_")[-1]
            process_path = os.path.join(processed_path, ('processed_data_' + end_name_path))
            file_processing.write_dict_to_json(final,process_path)
            logging.info(f"successful compute {file_name}")

    except Exception as e:
        logging.error(f"An unexpected error occurred in the main block: {e}")
        raise

handler()