import streamlit as st
import os
import pandas as pd 


if not os.path.exists("uploads"):
    os.makedirs("uploads")

if not os.path.exists("exports"):
    os.makedirs("exports")

def get_rows(start , end , level):

    df = pd.DataFrame()
    for i in range(len(df_yes)):

        if (df_yes.iloc[i , 2] > start) and (df_yes.iloc[i , 2] < end) and (df_yes.iloc[i , 0] > level):

            df = pd.concat([df , df_yes.iloc[[i]]])


    return df




st.title("Excel Filter")


uploaded_file = st.file_uploader("Choose a excel file" , type = "xlsx")

if uploaded_file is not None:

    file_bytes = uploaded_file.read()

        # Construct full file path
    save_path = os.path.join("uploads", uploaded_file.name)

        # Write to the specified path
    with open(save_path, "wb") as f:
        f.write(file_bytes)

    st.success(f"File saved successfully to {save_path} 🎉")

    data = pd.read_excel(save_path) 
    # print(len(data))
    # print(len(data)) # Replace "Sheet1" with your sheet name
    data["Numbeer"] = data["Numbeer"].apply(lambda x: x[2:] if isinstance(x, str) else x)
    data["Level"] = data["Level"].apply(lambda x: x[-1] if isinstance(x, str) else x)
    data["Level"] = pd.to_numeric(data["Level"], errors='coerce').astype('Int64')  # Use 'Int64' to handle NaNs

    data["Numbeer"] = pd.to_numeric(data["Numbeer"], errors='coerce').astype('Int64')  # Use 'Int64' to handle NaNs
    # data1 = data.copy()
    # data = data[["Level" , "Numbeer" , "Ser"]]
    # Display the first few rows of the dataframe
    demo = data.copy()
    # data.head()
    # data.info()

#___________________________________________________________________________________________________________________________________________________________



    level_1 = demo[demo["Level"] == 1] 
    level_1_yes = level_1[level_1["Ser"] == "Yes"]
    level_1_no = level_1[demo["Ser"] == "No"]


    level_2 = demo[demo["Level"] == 2]
    level_2_yes = level_2[level_2["Ser"] == "Yes"]
    level_2_no = level_2[demo["Ser"] == "No"]


    # Filter for Level 3
    level_3 = demo[demo["Level"] == 3]
    level_3_yes = level_3[level_3["Ser"] == "Yes"]
    level_3_no = level_3[level_3["Ser"] == "No"]

    # Filter for Level 4
    level_4 = demo[demo["Level"] == 4]
    level_4_yes = level_4[level_4["Ser"] == "Yes"]
    level_4_no = level_4[level_4["Ser"] == "No"]

    # Filter for Level 5
    level_5 = demo[demo["Level"] == 5]
    level_5_yes = level_5[level_5["Ser"] == "Yes"]
    level_5_no = level_5[level_5["Ser"] == "No"]

    # Filter for Level 6
    level_6 = demo[demo["Level"] == 6]
    level_6_yes = level_6[level_6["Ser"] == "Yes"]
    level_6_no = level_6[level_6["Ser"] == "No"]

    # Filter for Level 7
    level_7 = demo[demo["Level"] == 7]
    level_7_yes = level_7[level_7["Ser"] == "Yes"]
    level_7_no = level_7[level_7["Ser"] == "No"]


#___________________________________________________________________________________________________________________________________________



# Concatenate all 'yes' DataFrames into a single DataFrame
    df_yes = pd.concat(
    [
        level_1_yes,
        level_2_yes,
        level_3_yes,
        level_4_yes,
        level_5_yes,
        level_6_yes,
        level_7_yes
    ],
    ignore_index=True
)

# # Print the combined DataFrame
# len(df_yes)


# Concatenate all 'no' DataFrames into a single DataFrame
    df_no = pd.concat(
    [
        level_1_no,
        level_2_no,
        level_3_no,
        level_4_no,
        level_5_no,
        level_6_no,
        level_7_no
    ],
    ignore_index=True
)


#______________________________________________________________________________________________________________________________

    final = pd.DataFrame()

    for i in range(1 , len(df_no) - 1):


        print("*" * 100)
        print(df_no.iloc[i , 1] + 1 , df_no.iloc[i + 1 , 1])
        if ((df_no.iloc[i , 1] + 1) != (df_no.iloc[i + 1 , 1])):
            
            print("Inside IF")
            df = get_rows(df_no.iloc[i , 2] , df_no.iloc[i + 1 , 2] , df_no.iloc[i , 0])
            if len(df):

                final = pd.concat([final , df_no.iloc[[i]]])
                final = pd.concat([final , df])

        # elif (final.iloc[-1 , ] == (df_no.iloc[i + 1 , 1])):

            
        #     print("Appending next row")
        #     final.iloc[-1, :] = df_no.iloc[i, :]
        #     print(df_no.iloc[[i]])
        #     print(final.iloc[[-1]])


        print("*" * 100)


#_______________________________________________________________________________________________________________________________________

    final.to_excel("exports/filtered.xlsx")

    with open("exports/filtered.xlsx", "rb") as file:
        btn = st.download_button(
        label="Download",
        data=file,
        file_name="filtered.xlsx",
        mime="xlsx",
        )