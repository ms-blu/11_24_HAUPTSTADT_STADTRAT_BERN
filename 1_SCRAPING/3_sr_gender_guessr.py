import pandas as pd
import gender_guesser.detector as gender

def guess_gender(name):
    d = gender.Detector()
    return d.get_gender(name)

def extract_first_name(full_name):
    return full_name.split()[0]

def main():
    # Read the Excel file
    # Member names are exported from dataset and include Stadtrat + Gemeinderat.
    df = pd.read_excel("sr_gender_list.xlsx")

    # Extract the first name and remove middle names
    df["First Name"] = df["speaker_fullname"].apply(extract_first_name)

    # Guess gender for each first name
    df["Gender"] = df["First Name"].apply(guess_gender)

    # Save the updated DataFrame back to Excel
    df.to_excel("stadtrat_gender_guessed.xlsx", index=False)

if __name__ == "__main__":
    main()
