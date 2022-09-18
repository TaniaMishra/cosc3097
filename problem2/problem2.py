import pandas as pd

output = open("output.txt", "a")

icpc_data = pd.read_csv("icpc_input.txt", sep="    ", header=None, engine='python')   
print(icpc_data)
outside_data = pd.read_csv("outside_input.txt", sep="    ", header=None, engine='python')
print(outside_data)

icpc_incorrect_data = []
outside_incorrect_data = []

for index, row in icpc_data.iterrows():
    icpc_first_name = icpc_data.iat[index, 0].lower()
    icpc_last_name = icpc_data.iat[index, 1].lower()
    icpc_email = icpc_data.iat[index, 2].lower()
    outside_first_name_col = outside_data[0].str.lower()
    outside_last_name_col = outside_data[1].str.lower()
    outside_email_col = outside_data[2].str.lower()
    matching_data = outside_data[((outside_first_name_col == icpc_first_name) & (outside_last_name_col == icpc_last_name)) | (outside_email_col == icpc_email)]
    # print(f"{icpc_first_name}: {matching_data}")
    if (matching_data.size == 0):
        icpc_incorrect_data.append(row[2] + " " + row[1] + " " + row[0])
    # wrong_first_names = outside_data[outside_data[0] != row[0]].index
    # for row_index in wrong_first_names:
    #     icpc = "I " + row[2] + " " + row[1] + " " + row[0]
    #     outside = "O " + outside_data[2][row_index] + " " + outside_data[1][row_index] + " " + outside_data[0][row_index]
    #     if (icpc not in icpc_incorrect_data and outside not in outside_incorrect_data):
    #         outside_incorrect_data.append("O " + outside_data[2][row_index] + " " + outside_data[1][row_index] + " " + outside_data[0][row_index])
    #         icpc_incorrect_data.append("I " + row[2] + " " + row[1] + " " + row[0])
    # wrong_last_names = outside_data[outside_data[1] != row[1]].index
    # for row_index in wrong_last_names:
    #     icpc = "I " + row[2] + " " + row[1] + " " + row[0]
    #     outside = "O " + outside_data[2][row_index] + " " + outside_data[1][row_index] + " " + outside_data[0][row_index]
    #     if (icpc not in icpc_incorrect_data and outside not in outside_incorrect_data):
    #         outside_incorrect_data.append("O " + outside_data[2][row_index] + " " + outside_data[1][row_index] + " " + outside_data[0][row_index])
    #         icpc_incorrect_data.append("I " + row[2] + " " + row[1] + " " + row[0])
    # wrong_emails = outside_data[outside_data[2] != row[2]].index
    # for row_index in wrong_emails:
    #     icpc = "I " + row[2] + " " + row[1] + " " + row[0]
    #     outside = "O " + outside_data[2][row_index] + " " + outside_data[1][row_index] + " " + outside_data[0][row_index]
    #     if (icpc not in icpc_incorrect_data and outside not in outside_incorrect_data):
    #         outside_incorrect_data.append("O " + outside_data[2][row_index] + " " + outside_data[1][row_index] + " " + outside_data[0][row_index])
    #         icpc_incorrect_data.append("I " + row[2] + " " + row[1] + " " + row[0])

for index, row in outside_data.iterrows():
    outside_first_name = outside_data.iat[index, 0].lower()
    outside_last_name = outside_data.iat[index, 1].lower()
    outside_email = outside_data.iat[index, 2].lower()
    icpc_first_name_col = icpc_data[0].str.lower()
    icpc_last_name_col = icpc_data[1].str.lower()
    icpc_email_col = icpc_data[2].str.lower()
    matching_data = icpc_data[((icpc_first_name_col == outside_first_name) & (icpc_last_name_col == outside_last_name)) | (icpc_email_col == outside_email)]
    if (matching_data.size == 0):
        outside_incorrect_data.append(row[2] + " " + row[1] + " " + row[0])

print(outside_incorrect_data)
print(icpc_incorrect_data)

if (len(icpc_incorrect_data) == 0):
    output.write("No mismatches.")
else:
    icpc_incorrect_data.sort()
    outside_incorrect_data.sort()
    for element in icpc_incorrect_data:
        output.write(f"I {element}\n")
    for element in outside_incorrect_data:
        output.write(f"O {element}\n")


output.close()