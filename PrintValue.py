sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
            }
        }
    }
}

# for k1,v1 in sampleDict.items():
#     for k2,v2 in v1.items():
#         for k3,v3 in v2.items():
#             for k4 in v3:
#                 print(k4)
print(sampleDict['class']['student']['marks']['history'])