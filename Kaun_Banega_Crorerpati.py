qus=[["Who score fastest double hundread","Rohit Sharma","Chris Gayle","Virendra sehwag","Ishan Kishan",4],
     ["Younger to Score double hundread in odi","Subhman gill","chris Gayle","Sachin Tendulkar","Ishan Kishan",1],
     ["Highest wicket taker in history of IPL ","Dwayne Bravo","Yuzvendra Chahal","Piyush Chawla","Lasith Malinga",2],
     ["Who score fastest century in history of ipl","Chris Gayle","AB Devillers","David Miller","Quinton De cock",1],
     ["Who score fastest t20 century in history of t20 international","Chris Gayle","AB Devillers","David Miller","Quinton De cock",3],
     ["Who score fastest odi century in history of odi international","Shahid Afridi","AB Devillers","Virat kohli","CJ Anderson",2],
     ["Highest individual score in limit over of Cricket","264","298","308","208",1],
     ["Who Score 264 in limited over format","Chris Gayle","Rohit Sharma","Virat Kohli","AB Devillers",2],
     ["Highest individual score of Virat Kohli in limited over format","238","183","208","209",2],
     ["who hit longest six in International Cricket","Shahid Afridi","M S Dhoni","Liam Livingstone","C J Anderson",1],
     ["Highest Speed of spin bowled by in international Cricket","Ravichandra Ashwin","Shadab Khan","Shahid Afridi","Piyush Chawla",3],
     ["Highest Speed of fast bowled by in international Cricket","Mitchell Starc","Mitchell Johnson","Bret Lee","Shoaib Akhtar",4],
     ["Longest Six in history of ipl","125","115","114","130",1],
     ["Most Expensive foreign player of ipl 2022","Sam Curran","Mitchel Marsh","Liam Livingstone","Trent Boult",3],
     ["Who hit most number of six in international cricket","Rohit Sharma","Shahid Afridi","Chris Gayle","Ben Stokes",3]]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,640000,1250000,2500000,5000000,10000000]
mon=0
for i in range(len(qus)):
    print(f"\n\nQ.{i+1}>\t {qus[i][0]}")
    print(f"\ni.{qus[i][1]}\t\tii.{qus[i][2]}")
    print(f"iii.{qus[i][3]}\t\tiv.{qus[i][4]}")
    ans=int(input("\nEnter correct option"))
    if ans==0:
        mon=levels[i-1]
        break
    if ans==qus[i][5]:
        print(f"\nYou choose correct option you won {levels[i]}")
        if(i == 4):
          mon = 10000
        elif(i == 9):
          mon = 320000
        elif(i == 14):
          mon = 10000000
    else:
       print("\nYou choose wrong answer")
       break
print(f"You won Rs. {mon}")