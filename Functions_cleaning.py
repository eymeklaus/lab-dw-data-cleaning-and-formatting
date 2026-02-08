def standarized_gender_f(gender):
    if gender in ["Femal", "female", "F"]:
        return "F"
    elif gender in ["Male", "M"]:
        return "M"
    else:
        return gender
    

    df['new_gender'] = df['GENDER'].apply(standarized_gender)