import json
import requests
import time

# File paths
# Data last requestesed on 2024/10/14
# File SR_allSegments.json is manually loaded from here: https://bern.recapp.ch/viewer/api/shareparl/agendaItems?ios=false&language=de
# -> an overview of all SegmentUID which is the way in which Recapp divides data into segments. Each segment has a unique ID.
input_file = 'SR_allSegments.json'
output_file = '01_output/aggregated_responses_08_20.json'

# Base URL with placeholder
base_url = 'https://bern.recapp.ch/viewer/api/shareparl/segments?agendaItemUid={value}&ios=false&language=de'
# Headers for the requests, including contact information
headers = {
    'User-Agent': 'Mozilla/5.0',
    'From': 'Abfrage für Datenjournalismus-Projekt. Fragen bitte an: linus.kueng@gmail.com'
}


def fetch_data(agenda_item_uid):
    """Fetch data from the constructed URL."""
    url = base_url.replace('{value}', agenda_item_uid)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data for UID {agenda_item_uid}: {e}")
        return None


def main():
    """Read json, fetch and dump json"""
    try:
        # Read the input JSON file
        with open(input_file, 'r') as infile:
            data = json.load(infile)

        # Check if the data is a list
        if not isinstance(data, list):
            print("Input data is not a list.")
            return

        aggregated_responses = []

        # Process all items
        for item in data:
            agenda_item_uid = item.get('agendaItemUid')
            if agenda_item_uid:
                print(f"Fetching data for UID: {agenda_item_uid}")
                response_data = fetch_data(agenda_item_uid)
                if response_data:
                    aggregated_responses.append(response_data)
                    print(f"Data fetched successfully for UID: {agenda_item_uid}")
                # Adding a delay to avoid rate limiting
                time.sleep(1)  # 1-second delay between requests
            else:
                print(f"No 'agendaItemUid' found in item: {item}")

        # Save the aggregated responses to the output JSON file
        with open(output_file, 'w') as outfile:
            json.dump(aggregated_responses, outfile, indent=4)

        print(f"Data aggregation complete. Responses saved to {output_file}")

    except (IOError, json.JSONDecodeError) as e:
        print(f"Error reading or parsing input file: {e}")


if __name__ == "__main__":
    main()
