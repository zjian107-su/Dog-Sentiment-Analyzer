import argparse
import os
from os import listdir
from os.path import isfile, join
from automl_vision_predict import predict
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command")

    predict_parser = subparsers.add_parser("predict", help=predict.__doc__)
    predict_parser.add_argument("model_id")
    predict_parser.add_argument("score_threshold", nargs="?", default="")

    project_id = os.environ["PROJECT_ID"]
    compute_region = os.environ["REGION_NAME"]

    args = parser.parse_args()

    if args.command == "predict":
        onlyfiles = [f for f in listdir("./resources") if isfile(join("./resources", f))]
        #Reset the file
        os.remove("resultSave.txt")
        print("File Removed!")
        with open ("resultSave.txt", "w") as f:
            print("File Created!")
        for f in onlyfiles:
            if f != ".DS_Store":
                print(f)
                predict(
                    project_id,
                    compute_region,
                    args.model_id,
                    "./resources/" + f,
                    args.score_threshold,
                )

    #New Version
    from collections import Counter
    import matplotlib.pyplot as plt

    print("\n-------MAKING NUMBERS--------------------------\n")
    #Read saved files
    with open("resultSave.txt", "r") as f:
        text=f.read()
        #print(text)

    #Make string into list    
    textList=text.split(", ")

    #delete the last item which is " "
    del textList[-1]
    print(textList)

    flowerTypeList = textList
    countDic=Counter(flowerTypeList) #imported module
    print(countDic)
    print("")

    #show all keys & values
    total=0
    typeNumber=0
    for key in countDic:
        total += countDic[key]
        print("%s has value of %s."%(key,str(countDic[key])))
        typeNumber += 1

    print('')
        



    #show all values
    for key in countDic:
        print("Percentage of %s is %s." %(key,str((countDic[key]/total))))
        
        

    #show total
    print("\n")
    print('--Total: '+ str(total))
    print('')
    print("--Type number: "+ str(typeNumber))
    print("\n")
        
        

    print("\n-------MAKING CHARTS--------------------------\n")
    colorList=['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','black','green','pink',]
    labels = []
    sizes =[]
    colors = []
    explode = []

    #append in lables & sizes
    loopNumber=0
    for key in countDic:
        labels.append(key)
        sizes.append(str((countDic[key]/total)))
        colors.append(colorList[loopNumber])
        explode.append(0)
        loopNumber += 1

    '''
        print(labels)
        print(sizes)
        print(colors)
        print(explode)
    '''  


    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()

        
        



