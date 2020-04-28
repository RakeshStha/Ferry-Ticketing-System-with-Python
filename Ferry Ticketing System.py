#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     10/02/2019
# Copyright:   (c) DELL 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
from datetime import datetime
global date
date = datetime.now().strftime("%d/%m/%y")

#----------------------MAIN MENU---------------------------

def main_menu():
    print("*"*40)
    print("********************FERRY TICKETING SYSTEM********************")
    print("**************************MAIN MENU********************")
    print("*"*40)
    print(" P- Purchase Ticket ")
    print(" V- View Seating Arrangement ")
    print(" Q- Quit the system\n\n")
    customer = str(input("Please enter your choice:- ").upper())
    if customer == "P":
        sub_menu()
    elif customer == "V":
        arrangement()
    elif customer == "Q":
        quit()
    else:
        print("<<<<<<ERROR>>>>>>")
        return sub_menu()

#----------------------SUB MENU---------------------------
def sub_menu():
    destination()
    ch1 = int(input("Please Select Your Destination:- "))
    if ch1 == 1:
        print("_"*40)
        print("B– to purchase ticket for Business class")
        print("E– to purchase ticket for Economy class")
        print("M– to return to the Main Menu")
        ch2 = str(input("Please enter your choice:- ").upper())
        if ch2 == "B":
            business2lang()
        elif ch2 == "E":
            economy2lang()
        elif ch2 == "M":
            main_menu()
        else:
            print("<<<<<INVALID>>>>>")
            return sub_menu()
    elif ch1 == 2:
        print("_"*40)
        print("B – to purchase ticket for Business class")
        print("E – to purchase ticket for Economy class")
        print("M – to return to Main Menu")
        ch2 = str(input("Please enter your choice:- ").upper())
        if ch2 == "B":
            business2penang()
        elif ch2 == "E":
            economy2penang()
        elif ch2 == "M":
            main_menu()
        else:
            print("<<<<<INVALID>>>>>")
            return sub_menu()
    else:
        print("<<<<<INVALID>>>>>")
        return sub_menu()


#----------------------BUSINESS CLASS 2 LANGKAWI---------------------------
def business2lang():
    global trip
    global trip_seat
    global trip_class
    global trip_ferry
    print("-"*40)
    des_time2lang()
    chse = int(input("Please Select:- "))
    if chse == 1:
        print("#"*40)
        ferryID_101_b()
        if 0 in ferry_101_b:
            chse_1 = str(input("Would You Like To Buy Ticket? Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_101_b[9] = 1
                trip = "PENANG----LANGKAWI"
                trip_class = "Business"
                trip_seat = "B10"
                trip_ferry = "101 | TIME: 10:00AM"
                user()
            elif chse_1 == "N":
                business2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return business2lang()
        elif 0 not in ferry_101_b:
            print("Sorry Sorry Next Trip is after 1 hour")
            chse_1 = str(input("You can choose economy, TypeY/N:- "))
            if chse_1 == "Y":
                economy2lang()
            elif chse_1 == "N":
                business2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return business2lang()
        else:
            print("<<<<<ERROR>>>>>")
            return business2lang()
    elif chse == 2:
        print("-"*40)
        ferryID_102_b()
        if 0 in ferry_102_b:
            chse_1 = str(input("Would You Like To Buy Ticket? Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_102_b[7] = 1
                trip = "PENANG----LANGKAWI"
                trip_class = "Business"
                trip_seat = "B09"
                trip_ferry = "102 | TIME: 11:00AM"
                user()
            elif chse_1 == "N":
                business2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return business2lang()
        elif 0 not in ferry_102_b:
            print("Sorry Sorry Next Trip is after 1 hour")
            chse_1 = str(input("You can choose economy, Type Y/N:- ").upper())
            if chse_1 == "Y":
                economy2lang()
            elif chse_1 == "N":
                business2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return business2lang()
        else:
            print("<<<<<ERROR>>>>>")
            return business2lang()
    elif chse == 3:
        print("*"*40)
        ferryID_103_b()
        if 0 in ferry_103_b:
            chse_1 = str(input("Would You Like To Buy Ticket? Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_103_b[9] = 1
                trip = "PENANG----LANGKAWI"
                trip_class = "Business"
                trip_seat = "B10"
                trip_ferry = "103 | TIME: 12:00PM"
                user()
            elif chse_1 == "N":
                business2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return business2lang()
        elif 0 not in ferry_103_b:
            print("Sorry Sorry Next Trip is after 1 hour")
            chse_1 = str(input("You can choose economy, Type Y/N:- ").upper())
            if chse_1 == "Y":
                economy2lang()
            elif chse_1 == "N":
                business2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return business2lang()
        else:
            print("<<<<<ERROR>>>>>")
            return business2lang()
    elif chse == 4:
        print("#"*40)
        ferryID_104_b()
        if 0 in ferry_104_b:
            chse_1 = str(input("Would You Like To Buy Ticket? Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_104_b[1] = 1
                trip = "PENANG----LANGKAWI"
                trip_class = "Business"
                trip_seat = "B02"
                trip_ferry = "104 | TIME: 1:00PM"
                user()
            elif chse_1 == "N":
                business2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return business2lang()
        elif 0 not in ferry_104_b:
            print("Sorry Sorry Next Trip is after 1 hour")
            chse_1 = str(input("You can choose economy,Type Y/N:- ").upper())
            if chse_1 == "Y":
                economy2lang()
            elif chse_1 == "N":
                business2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return business2lang()
        else:
            print("<<<<<ERROR>>>>>")
            return main_menu()
    elif chse == 5:
        print("#"*40)
        ferryID_105_b()
        if 0 in ferry_105_b:
            chse_1 = str(input("Would You Like TO Buy Ticket? Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_105_b[9] = 1
                trip = "PENANG----LANGKAWI"
                trip_class = "Business"
                trip_seat = "B10"
                trip_ferry = "105 | TIME: 2:00PM"
                user()
            elif chse_1 == "N":
                business2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return business2lang()
        elif 0 not in ferry_105_b:
            print("Sorry Sorry Next Trip is after 1 hour")
            chse_1 = str(input("You can choose economy, Type  Y/N:- "))
            if chse_1 == "Y":
                economy2lang()
            elif chse_1 == "N":
                business2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return business2lang()
        else:
            print("<<<<<ERROR>>>>>")
            return business2lang()
    elif chse == 6:
        print("#"*40)
        ferryID_106_b()
        if 0 in ferry_106_b:
            chse_1 = str(input("Would You Like To Buy Ticket? Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_106_b[9] = 1
                trip = "PENANG----LANGKAWI"
                trip_class = "Business"
                trip_seat = "B10"
                trip_ferry = "101 | TIME: 3:00PM"
                user()
            elif chse_1 == "N":
                business2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return business2lang()
        elif 0 not in ferry_106_b:
            print("Sorry Sorry Next Trip is after 1 hour")
            chse_1 = str(input("You can choose economy, Type Y/N:- "))
            if chse_1 == "Y":
                economy2lang()
            elif chse_1 == "N":
                business2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return business2lang()
        else:
            print("<<<<<ERROR>>>>>")
            return business2lang()
    elif chse == 7:
        print("#"*40)
        ferryID_107_b()
        if 0 in ferry_101_b:
            chse_1 = str(input("Would You Like To Buy Ticket?Type  Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_101_b[9] = 1
                trip = "PENANG----LANGKAWI"
                trip_class = "Business"
                trip_seat = "B10"
                trip_ferry = "107 | TIME: 4:00PM"
                user()
            elif chse_1 == "N":
                business2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return business2lang()
        elif 0 not in ferry_107_b:
            print("Sorry Sorry Next Trip is after 1 hour")
            chse_1 = str(input("You can choose economy,Type Y/N:- "))
            if chse_1 == "Y":
                economy2lang()
            elif chse_1 == "N":
                business2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return business2lang()
        else:
            print("<<<<<ERROR>>>>>")
            return business2lang()
    elif chse == 8:
        print("#"*40)
        ferryID_108_b()
        if 0 in ferry_108_b:
            chse_1 = str(input("Would You Like To Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_108_b[9] = 1
                trip = "PENANG----LANGKAWI"
                trip_class = "Business"
                trip_seat = "B10"
                trip_ferry = "108 | TIME: 5:00PM"
                user()
            elif chse_1 == "N":
                business2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return business2lang()
        elif 0 not in ferry_108_b:
            print("Sorry Sorry Next Trip is after 1 hour")
            chse_1 = str(input("You can choose economy,Type Y/N:- "))
            if chse_1 == "Y":
                economy2lang()
            elif chse_1 == "N":
                business2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return business2lang()
        else:
            print("<<<<<ERROR>>>>>")
            return business2lang()
    elif chse == 9:
        main_menu()
    else:
        print("<<<<<ERROR>>>>>")
        return business2lang()

#----------------------ECONOMY CLASS 2 LANGKAWI--------------------------
def economy2lang():
    global trip
    global trip_seat
    global trip_class
    global trip_ferry
    print("-"*40)
    des_time2lang()
    chse = int(input("Select:- "))
    if chse == 1:
        print("#"*40)
        ferryID_101_e()
        if 0 in ferry_101_e:
            chse_1 = str(input("Would You Like To Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_101_e[31] = 1
                trip = "PENANG----LANGKAWI"
                trip_class = "Economy"
                trip_seat = "E32"
                trip_ferry = "101 | TIME: 10:00AM"
                user()
            elif chse_1 == "N":
                economy2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return economy2lang()
        elif 0 not in ferry_101_e:
            print("Sorry Sorry Next Trip is after 1 hour")
            chse_1 = str(input("Would You Like To Change Time?Type Y/N:- ").upper())
            if chse_1 == "Y":
                economy2lang()
            elif chse_1 == "N":
                sub_menu()
            else:
                print("<<<<<ERROR>>>>>")
                return economy2lang()
        else:
            print("<<<<<ERROR>>>>")
            return economy2lang()
    elif chse == 2:
        print("#"*40)
        ferryID_102_e()
        if 0 in ferry_102_e:
            chse_1 = str(input("Woul You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_102_e[32] = 1
                trip = "PENANG----LANGKAWI"
                trip_class = "Economy"
                trip_seat = "E33"
                trip_ferry = "102 | TIME: 11:00AM"
                user()
            elif chse_1 == "N":
                economy2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return economy2lang()
        elif 0 not in ferry_102_e:
            print("Sorry Sorry Next Trip is after 1 hour")
            chse_1 = str(input("Would You Like To Change Time?Type  Y/N:- ").upper())
            if chse_1 == "Y":
                economy2lang()
            elif chse_1 == "N":
                sub_menu()
            else:
                print("<<<<<ERROR>>>>>")
                return economy2lang()
        else:
            print("<<<<<ERROR>>>>>")
            return economy2lang()
    elif chse == 3:
        print("#"*40)
        ferryID_103_e()
        if 0 in ferry_103_e:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                trip = "PENANG----LANGKAWI"
                trip_class = "Economy"
                trip_seat = "E40"
                trip_ferry = "103 | TIME: 12:00PM"
                user()
            elif chse_1 == "N":
                economy2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return economy2lang()
        elif 0 not in ferry_103_e:
            print("Sorry Sorry Next Trip is after 1 hour")
            chse_1 = str(input("Would You Like To Change Time?Type Y/N:- ").upper())
            if chse_1 == "Y":
                economy2lang()
            elif chse_1 == "N":
                sub_menu()
            else:
                print("<<<<<ERROR>>>>>")
                return economy2lang()
        else:
            print("<<<<<ERROR>>>>>")
            return economy2lang()
    elif chse == 4:
        print("#"*40)
        ferryID_104_e()
        if 0 in ferry_104_e:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_104_e[38] = 1
                trip = "PENANG----LANGKAWI"
                trip_class = "Economy"
                trip_seat = "E39"
                trip_ferry = "104 | TIME: 1:00PM"
                user()
            elif chse_1 == "N":
                economy2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return economy2lang()
        elif 0 not in ferry_104_e:
            print("Sorry Sorry Next Trip is after 1 hour")
            chse_1 = str(input("Would You Like To Change Time?Type Y/N:- ").upper())
            if chse_1 == "Y":
                economy2lang()
            elif chse_1 == "N":
                sub_menu()
            else:
                print("<<<<<ERROR>>>>>")
                return economy2lang()
        else:
            print("<<<<<ERROR>>>>>")
            return economy2lang()
    elif chse == 5:
        print("#"*40)
        ferryID_105_e()
        if 0 in ferry_105_e:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_105_e[31] = 1
                trip = "PENANG----LANGKAWI"
                trip_class = "Economy"
                trip_seat = "E32"
                trip_ferry = "101 | TIME: 2:00PM"
                user()
            elif chse_1 == "N":
                economy2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return economy2lang()
        elif 0 not in ferry_105_e:
            print("Sorry Sorry Next Trip is after 1 hour")
            chse_1 = str(input("Would You Like To Change Time?Type Y/N:- ").upper())
            if chse_1 == "Y":
                economy2lang()
            elif chse_1 == "N":
                sub_menu()
            else:
                print("<<<<<ERROR>>>>>")
                return economy2lang()
        else:
            print("<<<<<ERROR>>>>>>")
            return economy2lang()
    elif chse == 6:
        print("#"*40)
        ferryID_106_e()
        if 0 in ferry_105_e:
            chse_1 = str(input("Would You Like To Buy Ticket?TypeY/N:- ").upper())
            if chse_1 == "Y":
                ferry_106_e[31] = 1
                trip = "PENANG----LANGKAWI"
                trip_class = "Economy"
                trip_seat = "E32"
                trip_ferry = "106 | TIME: 3:00PM"
                user()
            elif chse_1 == "N":
                economy2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return economy2lang()
        elif 0 not in ferry_106_e:
            print("Sorry Sorry Next Trip is after 1 hour")
            chse_1 = str(input("Would You Like To Change Time?Type Y/N:- ").upper())
            if chse_1 == "Y":
                economy2lang()
            elif chse_1 == "N":
                sub_menu()
            else:
                print("<<<<<ERROR>>>>>")
                return economy2lang()
        else:
            print("<<<<<ERROR>>>>>")
            return economy2lang()
    elif chse == 7:
        print("-"*40)
        ferryID_105_e()
        if 0 in ferry_107_e:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_107_e[31] = 1
                trip = "PENANG----LANGKAWI"
                trip_class = "Economy"
                trip_seat = "E32"
                trip_ferry = "107 | TIME: 4:00PM"
                user()
            elif chse_1 == "N":
                economy2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return economy2lang()
        elif 0 not in ferry_107_e:
            print("Sorry Next Trip is after 1 hour")
            chse_1 = str(input("Would You Like To Change Time?Type Y/N:- ").upper())
            if chse_1 == "Y":
                economy2lang()
            elif chse_1 == "N":
                sub_menu()
            else:
                print("<<<<<ERROR>>>>>")
                return economy2lang()
        else:
            print("<<<<<ERROR>>>>>")
            return economy2lang()
    elif chse == 8:
        print("-"*40)
        ferryID_108_e()
        if 0 in ferry_108_e:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_108_e[31] = 1
                trip = "PENANG----LANGKAWI"
                trip_class = "Economy"
                trip_seat = "E32"
                trip_ferry = "108 | TIME: 5:00PM"
                user()
            elif chse_1 == "N":
                economy2lang()
            else:
                print("<<<<<ERROR>>>>>")
                return economy2lang()
        elif 0 not in ferry_108_e:
            print("Sorry Next Trip is after 1 hour")
            chse_1 = str(input("Would You Like To Change Time?Type Y/N:- ").upper())
            if chse_1 == "Y":
                economy2lang()
            elif chse_1 == "N":
                sub_menu()
            else:
                print("<<<<<ERROR>>>>>")
                return economy2lang()
        else:
            print("<<<<<ERROR>>>>>")
            return economy2lang()
    elif chse == 9:
        main_menu()
    else:
        print("<<<<<INVALID>>>>>")
        return business2lang()

#----------------------BUSINESS CLASS 2 PENANG---------------------------

def business2penang():
    global trip
    global trip_seat
    global trip_class
    global trip_ferry
    print("-"*40)
    des_time2penang()
    chse = int(input("Select:- "))
    if chse == 1:
        print("-"*40)
        ferryID_201_b()
        if 0 in ferry_201_b:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_201_b[1] = 1
                trip = "LANGKAWI----PENANG"
                trip_class = "Business"
                trip_seat = "B02"
                trip_ferry = "201 | TIME: 10:00AM"
                user()
            elif chse_1 == "N":
                business2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return business2penang()
        elif 0 not in ferry_201_b:
            print("Sorry Next Trip is after 1 hour")
            chse_1 = str(input("You can choose economy,Type Y/N:- ").upper())
            if chse_1 == "Y":
                economy()
            elif chse_1 == "N":
                business2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return business2penang()
        else:
            print("<<<<<INVALID>>>>>")
            return business2penang()
    elif chse == 2:
        print("-"*40)
        ferryID_202_b()
        if 0 in ferry_202_b:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_202_b[6] = 1
                trip = "LANGKAWI----PENANG"
                trip_class = "Business"
                trip_seat = "B07"
                trip_ferry = "202 | TIME: 11:00AM"
                user()
            elif chse_1 == "N":
                business2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return business2penang()
        elif 0 not in ferry_202_b:
            print("Sorry Next Trip is after 1 hour")
            chse_1 = str(input("You can choose economy,Type Y/N:- ").upper())
            if chse_1 == "Y":
                economy()
            elif chse_1 == "N":
                business2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return business2penang()
        else:
            print("<<<<<INVALID>>>>>")
            return business2penang()
    elif chse == 3:
        print("-"*40)
        ferryID_203_b()
        if 0 in ferry_203_b:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_203_b[4] = 1
                trip = "LANGKAWI----PENANG"
                trip_class = "Business"
                trip_seat = "B05"
                trip_ferry = "203 | TIME: 12:00PM"
                user()
            elif chse_1 == "N":
                business2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return business2penang()
        elif 0 not in ferry_203_b:
            print("Sorry Next Trip is after 1 hour")
            chse_1 = str(input("You can choose economy,Type Y/N:- ").upper())
            if chse_1 == "Y":
                economy()
            elif chse_1 == "N":
                business2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return business2penang()
        else:
            print("<<<<<INVALID>>>>>")
            return business2penang()
    elif chse == 4:
        print("-"*40)
        ferryID_204_b()
        if 0 in ferry_204_b:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_204_b[5] = 1
                trip = "LANGKAWI----PENANG"
                trip_class = "Business"
                trip_seat = "B06"
                trip_ferry = "204 | TIME: 1:00PM"
                user()
            elif chse_1 == "N":
                business2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return business2penang()
        elif 0 not in ferry_204_b:
            print("Sorry Next Trip is after 1 hour")
            chse_1 = str(input("You can choose economy,Type Y/N:- ").upper())
            if chse_1 == "Y":
                economy()
            elif chse_1 == "N":
                business2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return business2penang()
        else:
            print("<<<<<INVALID>>>>>")
            return main_menu()
    elif chse == 5:
        print("-"*40)
        ferryID_205_b()
        if 0 in ferry_205_b:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_205_b[1] = 1
                trip = "LANGKAWI----PENANG"
                trip_class = "Business"
                trip_seat = "B02"
                trip_ferry = "205 | TIME: 2:00PM"
                user()
            elif chse_1 == "N":
                business2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return business2penang()
        elif 0 not in ferry_205_b:
            print("Sorry Next Trip is after 1 hour")
            chse_1 = str(input("You can choose economy,Type Y/N:- ").upper())
            if chse_1 == "Y":
                economy()
            elif chse_1 == "N":
                business2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return business2penang()
        else:
            print("<<<<<INVALID>>>>>")
            return business2penang()
    elif chse == 6:
        print("-"*40)
        ferryID_206_b()
        if 0 in ferry_206_b:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_206_b[1] = 1
                trip = "LANGKAWI----PENANG"
                trip_class = "Business"
                trip_seat = "B02"
                trip_ferry = "206 | TIME: 3:00PM"
                user()
            elif chse_1 == "N":
                business2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return business2penang()
        elif 0 not in ferry_206_b:
            print("Sorry Next Trip is after 1 hour")
            chse_1 = str(input("You can choose economy,Type Y/N:- ").upper())
            if chse_1 == "Y":
                economy()
            elif chse_1 == "N":
                business2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return business2penang()
        else:
            print("<<<<<INVALID>>>>>")
            return business2penang()
    elif chse == 7:
        print("-"*40)
        ferryID_207_b()
        if 0 in ferry_207_b:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_207_b[1] = 1
                trip = "LANGKAWI----PENANG"
                trip_class = "Business"
                trip_seat = "B02"
                trip_ferry = "207 | TIME: 4:00PM"
                user()
            elif chse_1 == "N":
                business2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return business2penang()
        elif 0 not in ferry_207_b:
            print("Sorry Next Trip is after 1 hour")
            chse_1 = str(input("You can choose economy,Type Y/N:- ").upper())
            if chse_1 == "Y":
                economy()
            elif chse_1 == "N":
                business2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return business2penang()
        else:
            print("<<<<<INVALID>>>>>")
            return business2penang()
    elif chse == 8:
        print("-"*40)
        ferryID_205_b()
        if 0 in ferry_208_b:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_208_b[1] = 1
                trip = "LANGKAWI----PENANG"
                trip_class = "Business"
                trip_seat = "B02"
                trip_ferry = "208 | TIME: 5:00PM"
                user()
            elif chse_1 == "N":
                business2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return business2penang()
        elif 0 not in ferry_208_b:
            print("Sorry Next Trip is after 1 hour")
            chse_1 = str(input("You can choose economy,Type Y/N:- ").upper())
            if chse_1 == "Y":
                economy()
            elif chse_1 == "N":
                business2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return business2penang()
        else:
            print("<<<<<INVALID>>>>>")
            return business2penang()
    elif chse == 9:
        main_menu()
    else:
        print("<<<<<INVALID>>>>>")
        return business2penang()

#----------------------ECONOMY CLASS 2 PENANG--------------------------
def economy2penang():
    global trip
    global trip_seat
    global trip_class
    global trip_ferry
    print("-"*40)
    des_time2penang()
    chse = int(input("Select:- "))
    if chse == 1:
        print("-"*40)
        ferryID_201_e()
        if 0 in ferry_201_e:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_201_e[11] = 1
                trip = "LANGKAWI----PENANG"
                trip_class = "Economy"
                trip_seat = "E12"
                trip_ferry = "201 | TIME: 10:00AM"
                user()
            elif chse_1 == "N":
                economy2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return business2penang()
        elif 0 not in ferry_201_e:
            print("Sorry Next Trip is after 1 hour")
            chse_1 = str(input("Would You Like To Change Time?Type Y/N:- "))
            if chse_1 == "yes":
                des_time2penang()
            elif chse_1 == "no":
                economy2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return economy2penang()
        else:
            print("<<<<<INVALID>>>>>")
            return economy2penang()
    elif chse == 2:
        print("-"*40)
        ferryID_202_e()
        if 0 in ferry_202_e:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_202_e[37] = 1
                trip = "LANGKAWI----PENANG"
                trip_class = "Economy"
                trip_seat = "E38"
                trip_ferry = "202 | TIME: 11:00AM"
                user()
            elif chse_1 == "N":
                economy2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return economy2penang()
        elif 0 not in ferry_202_e:
            print("Sorry Next Trip is after 1 hour")
            chse_1 = str(input("Would You Like To Change Time?Type Y/N:- ").upper())
            if chse_1 == "Y":
                des_time2penang()
            elif chse_1 == "N":
                economy2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return economy2penang()
        else:
            print("<<<<<INVALID>>>>>")
            return economy2penang()
    elif chse == 3:
        print("-"*40)
        ferryID_203_e()
        if 0 in ferry_203_e:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_203_e[32] = 1
                trip = "LANGKAWI----PENANG"
                trip_class = "Economy"
                trip_seat = "E33"
                trip_ferry = "203 | TIME: 12:00PM"
                user()
            elif chse_1 == "N":
                economy2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return business2penang()
        elif 0 not in ferry_203_e:
            print("Sorry Next Trip is after 1 hour")
            chse_1 = str(input("Would You Like To Change Time?Type Y/N:- ").upper())
            if chse_1 == "Y":
                des_time2penang()
            elif chse_1 == "N":
                economy2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return economy2penang()
        else:
            print("<<<<<INVALID>>>>>")
            return economy2penang()
    elif chse == 4:
        print("-"*40)
        ferryID_204_e()
        if 0 in ferry_204_e:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_204_e[39] = 1
                trip = "LANGKAWI----PENANG"
                trip_class = "Economy"
                trip_seat = "E40"
                trip_ferry = "204 | TIME: 1:00PM"
                user()
            elif chse_1 == "N":
                economy2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return economy2penang()
        elif 0 not in ferry_204_e:
            print("Sorry Next Trip is after 1 hour")
            chse_1 = str(input("Would You Like To Change Time?Type Y/N:- ").upper())
            if chse_1 == "Y":
                des_time2penang()
            elif chse_1 == "N":
                economy2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return economy2penang()
        else:
            print("<<<<<INVALID>>>>>")
            return economy2penang()
    elif chse == 5:
        print("-"*40)
        ferryID_205_e()
        if 0 in ferry_205_e:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_205_e[37] = 1
                trip = "LANGKAWI----PENANG"
                trip_class = "Economy"
                trip_seat = "E38"
                trip_ferry = "205 | TIME: 2:00PM"
                user()
            elif chse_1 == "N":
                economy2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return economy2penang()
        elif 0 not in ferry_205_e:
            print("Sorry Next Trip is after 1 hour")
            chse_1 = str(input("Would You Like To Change Time?Type Y/N:- ").upper())
            if chse_1 == "Y":
                des_time2penang()
            elif chse_1 == "N":
                economy2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return economy2penang()
        else:
            print("<<<<<INVALID>>>>>")
            return economy2penang()
    elif chse == 6:
        print("-"*40)
        ferryID_202_e()
        if 0 in ferry_206_e:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_206_e[37] = 1
                trip = "LANGKAWI----PENANG"
                trip_class = "Economy"
                trip_seat = "E38"
                trip_ferry = "206 | TIME: 3:00PM"
                user()
            elif chse_1 == "N":
                economy2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return economy2penang()
        elif 0 not in ferry_206_e:
            print("Sorry Next Trip is after 1 hour")
            chse_1 = str(input("Would You Like To Change Time?Type Y/N:- ").upper())
            if chse_1 == "Y":
                des_time2penang()
            elif chse_1 == "N":
                economy2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return economy2penang()
        else:
            print("<<<<<INVALID>>>>>")
            return economy2penang()
    elif chse == 7:
        print("-"*40)
        ferryID_207_e()
        if 0 in ferry_207_e:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_207_e[37] = 1
                trip = "LANGKAWI----PENANG"
                trip_class = "Economy"
                trip_seat = "E38"
                trip_ferry = "207 | TIME: 4:00PM"
                user()
            elif chse_1 == "N":
                economy2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return economy2penang()
        elif 0 not in ferry_207_e:
            print("Sorry Next Trip is after 1 hour")
            chse_1 = str(input("Would You Like To Change Time?Type Y/N:- ").upper())
            if chse_1 == "Y":
                des_time2penang()
            elif chse_1 == "N":
                economy2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return economy2penang()
        else:
            print("<<<<<INVALID>>>>>")
            return economy2penang()
    elif chse == 8:
        print("-"*40)
        ferryID_208_e()
        if 0 in ferry_208_e:
            chse_1 = str(input("Would You Like To Buy Ticket?Type Y/N:- ").upper())
            if chse_1 == "Y":
                ferry_208_e[37] = 1
                trip = "LANGKAWI----PENANG"
                trip_class = "Economy"
                trip_seat = "E38"
                trip_ferry = "208 | TIME: 5:00PM"
                user()
            elif chse_1 == "N":
                economy2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return economy2penang()
        elif 0 not in ferry_208_e:
            print("Sorry Next Trip is after 1 hour")
            chse_1 = str(input("Would You Like To Change Time?Type Y/N:- ").upper())
            if chse_1 == "Y":
                des_time2penang()
            elif chse_1 == "N":
                economy2penang()
            else:
                print("<<<<<INVALID>>>>>")
                return economy2penang()
        else:
            print("<<<<<INVALID>>>>>")
            return economy2penang()
    elif chse == 9:
        main_menu()
    else:
        print("<<<<<INVALID>>>>>")
        return economy2penang()

def user():
    print("-"*40)
    global f_name
    global l_name
    f_name = str(input("Enter Your First Name:- ").title())
    l_name = str(input("Enter Your Last Name:- ").title())
    purchase()

def purchase():
    print("\n"*20)
    print("*"*17, "Thank You", "*"*17)
    print("* Destination: ", trip)
    print("*"*45)
    print("* FERRY ID: ", trip_ferry, date)
    print("* Class:    ", trip_class)
    print("* Name :    ", f_name, l_name)
    print("*"*45)
    print("\n--[1] Back to Main Menu--[2] Quit--")
    ticket()
    ch2 = int(input("Enter:- "))
    if ch2 == 1:
        main_menu()
    elif ch2 == 2:
        quit()
    else:
        quit()

def ticket():
    file = open("Ticket.txt", "w")
    print("*"*17, "Thank You", "*"*17, file = open("Ticket.txt", "a"))
    print("* Destination: ", trip, file = open("Ticket.txt", "a"))
    print("*"*45, file = open("Ticket.txt", "a"))
    print("* FERRY ID: ", trip_ferry, date, file = open("Ticket.txt", "a"))
    print("* Class:    ", trip_class, file = open("Ticket.txt", "a"))
    print("* Name :    ", f_name, l_name, file = open("Ticket.txt", "a"))
    print("*"*45, file = open("Ticket.txt", "a"))
    file.close()

def fer_ID():
    print("*"*29)
    print("*     PENANG ---> LANGKAWI    ")
    print("-"*29)
    print("Ferry ID: 101 -------- 10:00AM")
    print("Ferry ID: 102 -------- 11:00AM")
    print("Ferry ID: 103 -------- 12:00PM")
    print("Ferry ID: 104 -------- O1:00PM")
    print("Ferry ID: 105 -------- 02:00PM")
    print("Ferry ID: 106 -------- 03:00PM")
    print("Ferry ID: 107 -------- 04:00PM")
    print("Ferry ID: 108 -------- 05:00PM")
    print("*"*29)
    print("*     LANGKAWI ---> PENANG    ")
    print("-"*29)
    print("Ferry ID: 201 -------- 10:00AM")
    print("Ferry ID: 202 -------- 11:00AM")
    print("Ferry ID: 203 -------- 12:00PM")
    print("Ferry ID: 204 -------- O1:00PM")
    print("Ferry ID: 205 -------- 02:00PM")
    print("Ferry ID: 206 -------- 03:00PM")
    print("Ferry ID: 207 -------- 04:00PM")
    print("Ferry ID: 208 -------- 05:00PM")
    print("*"*29)
    type = input("TYPE ANY BUTTON TO BACK MAIN MENU:- ")
    if type == "":
        main_menu()
    else:
        main_menu()

def destination():
    print("-"*40)
    print("*"*40)
    print("*     CHOOSE DESTINATION     *")
    print("*"*40)
    print("[1] Penang -----> Langkawi")
    print("[2] Langkawi -----> Penang")
    print("[3] Back\n")

def des_time2lang():
    print("\nSelect Time:")
    print("\n[1]-10:00AM\n[2]-11:00AM\n[3]-12:OOPM\n[4]-01:00PM\n[5]-02:00PM\n[6]-03:00PM\n[7]-04:00PM\n[8]-05:00PM\n[9]-Back to Main Menu")

def des_time2penang():
    print("\nSelect Time:")
    print("\n[1]-10:00AM\n[2]-11:00AM\n[3]-12:OOPM\n[4]-01:00PM\n[5]-02:00PM\n[6]-03:00PM\n[7]-04:00PM\n[8]-05:00PM\n[9]-Back to Main Menu")

def arrangement():
    destination()
    way_1 = int(input("\nCheck Your Destination:- "))
    if way_1 == 1:
        des_time2lang()
        ch1 = int(input("\nSelect Time:- "))
        if ch1 == 1:
            ferryID_101()
            main_menu()
        elif ch1 == 2:
            ferryID_102()
            main_menu()
        elif ch1 == 3:
            ferryID_103()
            main_menu()
        elif ch1 == 4:
            ferryID_104()
            main_menu()
        elif ch1 == 5:
            ferryID_105()
            main_menu()
        elif ch1==6:
            main_menu()
        elif ch1==7:
            main_menu()
        elif ch1==8:
            main_menu()
        else:
            print("Error Value")
            return destination()
    elif way_1 == 2:
        des_time2penang()
        ch1 = int(input("\nSelect Time: "))
        if ch1 == 1:
            ferryID_201()
            main_menu()
        elif ch1 == 2:
            ferryID_202()
            main_menu()
        elif ch1 == 3:
            ferryID_203()
            main_menu()
        elif ch1 == 4:
            ferryID_204()
            main_menu()
        elif ch1 == 5:
            main_menu()
        elif ch1 == 6:
            main_menu()
        elif ch1 == 7:
            main_menu()
        elif ch1 == 8:
            main_menu()
        else:
            print("Error Value")
            return destination()
    else:
        print("Error Value")
        return arrangement()

#----------------------FERRY ID FOR LANGKAWI----------------------------
#FerryID 1:
ferry_101_b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
ferry_101_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_101_b():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 101                        Time: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_101_b[0], "     *     ",ferry_101_b[1], "     *     ",ferry_101_b[2], "     *     ",ferry_101_b[3], "     *     ",ferry_101_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_b[5], "     *     ",ferry_101_b[6], "     *     ",ferry_101_b[7], "     *     ",ferry_101_b[8], "     *     ",ferry_101_b[9], "     *")
    print("***********************************************************************")
def ferryID_101_e():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 101                        Time: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[11], "     *     ",ferry_101_e[12], "     *     ",ferry_101_e[13], "     *     ",ferry_101_e[14], "     *     ",ferry_101_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[16], "     *     ",ferry_101_e[17], "     *     ",ferry_101_e[18], "     *     ",ferry_101_e[19], "     *     ",ferry_101_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[21], "     *     ",ferry_101_e[22], "     *     ",ferry_101_e[23], "     *     ",ferry_101_e[24], "     *     ",ferry_101_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[26], "     *     ",ferry_101_e[27], "     *     ",ferry_101_e[28], "     *     ",ferry_101_e[29], "     *     ",ferry_101_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[31], "     *     ",ferry_101_e[32], "     *     ",ferry_101_e[33], "     *     ",ferry_101_e[34], "     *     ",ferry_101_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[36], "     *     ",ferry_101_e[37], "     *     ",ferry_101_e[38], "     *     ",ferry_101_e[39], "     *     ",ferry_101_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[41], "     *     ",ferry_101_e[42], "     *     ",ferry_101_e[43], "     *     ",ferry_101_e[44], "     *     ",ferry_101_e[45], "     *")
    print("***********************************************************************")


def ferryID_101():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 101                        Time: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_101_b[0], "     *     ",ferry_101_b[1], "     *     ",ferry_101_b[2], "     *     ",ferry_101_b[3], "     *     ",ferry_101_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_b[5], "     *     ",ferry_101_b[6], "     *     ",ferry_101_b[7], "     *     ",ferry_101_b[8], "     *     ",ferry_101_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[11], "     *     ",ferry_101_e[12], "     *     ",ferry_101_e[13], "     *     ",ferry_101_e[14], "     *     ",ferry_101_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[16], "     *     ",ferry_101_e[17], "     *     ",ferry_101_e[18], "     *     ",ferry_101_e[19], "     *     ",ferry_101_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[21], "     *     ",ferry_101_e[22], "     *     ",ferry_101_e[23], "     *     ",ferry_101_e[24], "     *     ",ferry_101_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[26], "     *     ",ferry_101_e[27], "     *     ",ferry_101_e[28], "     *     ",ferry_101_e[29], "     *     ",ferry_101_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[31], "     *     ",ferry_101_e[32], "     *     ",ferry_101_e[33], "     *     ",ferry_101_e[34], "     *     ",ferry_101_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[36], "     *     ",ferry_101_e[37], "     *     ",ferry_101_e[38], "     *     ",ferry_101_e[39], "     *     ",ferry_101_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[41], "     *     ",ferry_101_e[42], "     *     ",ferry_101_e[43], "     *     ",ferry_101_e[44], "     *     ",ferry_101_e[45], "     *")
    print("***********************************************************************")




#FerryID 2:
ferry_102_b = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
ferry_102_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_102_b():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 102                        Time: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_102_b[0], "     *     ",ferry_102_b[1], "     *     ",ferry_102_b[2], "     *     ",ferry_102_b[3], "     *     ",ferry_102_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_b[5], "     *     ",ferry_102_b[6], "     *     ",ferry_102_b[7], "     *     ",ferry_102_b[8], "     *     ",ferry_102_b[9], "     *")
    print("***********************************************************************")
def ferryID_102_e():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 102                        Time: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[11], "     *     ",ferry_102_e[12], "     *     ",ferry_102_e[13], "     *     ",ferry_102_e[14], "     *     ",ferry_102_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[16], "     *     ",ferry_102_e[17], "     *     ",ferry_102_e[18], "     *     ",ferry_102_e[19], "     *     ",ferry_102_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[21], "     *     ",ferry_102_e[22], "     *     ",ferry_102_e[23], "     *     ",ferry_102_e[24], "     *     ",ferry_102_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[26], "     *     ",ferry_102_e[27], "     *     ",ferry_102_e[28], "     *     ",ferry_102_e[29], "     *     ",ferry_102_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[31], "     *     ",ferry_102_e[32], "     *     ",ferry_102_e[33], "     *     ",ferry_102_e[34], "     *     ",ferry_102_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[36], "     *     ",ferry_102_e[37], "     *     ",ferry_102_e[38], "     *     ",ferry_102_e[39], "     *     ",ferry_102_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[41], "     *     ",ferry_102_e[42], "     *     ",ferry_102_e[43], "     *     ",ferry_102_e[44], "     *     ",ferry_102_e[45], "     *")
    print("***********************************************************************")



def ferryID_102():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 102                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_102_b[0], "     *     ",ferry_102_b[1], "     *     ",ferry_102_b[2], "     *     ",ferry_102_b[3], "     *     ",ferry_102_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_b[5], "     *     ",ferry_102_b[6], "     *     ",ferry_102_b[7], "     *     ",ferry_102_b[8], "     *     ",ferry_102_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[11], "     *     ",ferry_102_e[12], "     *     ",ferry_102_e[13], "     *     ",ferry_102_e[14], "     *     ",ferry_102_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[16], "     *     ",ferry_102_e[17], "     *     ",ferry_102_e[18], "     *     ",ferry_102_e[19], "     *     ",ferry_102_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[21], "     *     ",ferry_102_e[22], "     *     ",ferry_102_e[23], "     *     ",ferry_102_e[24], "     *     ",ferry_102_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[26], "     *     ",ferry_102_e[27], "     *     ",ferry_102_e[28], "     *     ",ferry_102_e[29], "     *     ",ferry_102_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[31], "     *     ",ferry_102_e[32], "     *     ",ferry_102_e[33], "     *     ",ferry_102_e[34], "     *     ",ferry_102_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[36], "     *     ",ferry_102_e[37], "     *     ",ferry_102_e[38], "     *     ",ferry_102_e[39], "     *     ",ferry_102_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[41], "     *     ",ferry_102_e[42], "     *     ",ferry_102_e[43], "     *     ",ferry_102_e[44], "     *     ",ferry_102_e[45], "     *")
    print("***********************************************************************")



#FerryID 3:
ferry_103_b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
ferry_103_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
def ferryID_103_b():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 103                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_103_b[0], "     *     ",ferry_103_b[1], "     *     ",ferry_103_b[2], "     *     ",ferry_103_b[3], "     *     ",ferry_103_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_b[5], "     *     ",ferry_103_b[6], "     *     ",ferry_103_b[7], "     *     ",ferry_103_b[8], "     *     ",ferry_103_b[9], "     *")
    print("***********************************************************************")
def ferryID_103_e():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 103                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[11], "     *     ",ferry_103_e[12], "     *     ",ferry_103_e[13], "     *     ",ferry_103_e[14], "     *     ",ferry_103_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[16], "     *     ",ferry_103_e[17], "     *     ",ferry_103_e[18], "     *     ",ferry_103_e[19], "     *     ",ferry_103_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[21], "     *     ",ferry_103_e[22], "     *     ",ferry_103_e[23], "     *     ",ferry_103_e[24], "     *     ",ferry_103_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[26], "     *     ",ferry_103_e[27], "     *     ",ferry_103_e[28], "     *     ",ferry_103_e[29], "     *     ",ferry_103_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[31], "     *     ",ferry_103_e[32], "     *     ",ferry_103_e[33], "     *     ",ferry_103_e[34], "     *     ",ferry_103_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[36], "     *     ",ferry_103_e[37], "     *     ",ferry_103_e[38], "     *     ",ferry_103_e[39], "     *     ",ferry_103_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[41], "     *     ",ferry_103_e[42], "     *     ",ferry_103_e[43], "     *     ",ferry_103_e[44], "     *     ",ferry_103_e[45], "     *")
    print("***********************************************************************")



def ferryID_103():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 103                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_103_b[0], "     *     ",ferry_103_b[1], "     *     ",ferry_103_b[2], "     *     ",ferry_103_b[3], "     *     ",ferry_103_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_b[5], "     *     ",ferry_103_b[6], "     *     ",ferry_103_b[7], "     *     ",ferry_103_b[8], "     *     ",ferry_103_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[11], "     *     ",ferry_103_e[12], "     *     ",ferry_103_e[13], "     *     ",ferry_103_e[14], "     *     ",ferry_103_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[16], "     *     ",ferry_103_e[17], "     *     ",ferry_103_e[18], "     *     ",ferry_103_e[19], "     *     ",ferry_103_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[21], "     *     ",ferry_103_e[22], "     *     ",ferry_103_e[23], "     *     ",ferry_103_e[24], "     *     ",ferry_103_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[26], "     *     ",ferry_103_e[27], "     *     ",ferry_103_e[28], "     *     ",ferry_103_e[29], "     *     ",ferry_103_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[31], "     *     ",ferry_103_e[32], "     *     ",ferry_103_e[33], "     *     ",ferry_103_e[34], "     *     ",ferry_103_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[36], "     *     ",ferry_103_e[37], "     *     ",ferry_103_e[38], "     *     ",ferry_103_e[39], "     *     ",ferry_103_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[41], "     *     ",ferry_103_e[42], "     *     ",ferry_103_e[43], "     *     ",ferry_103_e[44], "     *     ",ferry_103_e[45], "     *")
    print("***********************************************************************")




#FerryID 4:
ferry_104_b = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ferry_104_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_104_b():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 104                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_104_b[0], "     *     ",ferry_104_b[1], "     *     ",ferry_104_b[2], "     *     ",ferry_104_b[3], "     *     ",ferry_104_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_b[5], "     *     ",ferry_104_b[6], "     *     ",ferry_104_b[7], "     *     ",ferry_104_b[8], "     *     ",ferry_104_b[9], "     *")
    print("***********************************************************************")
def ferryID_104_e():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 104                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[11], "     *     ",ferry_104_e[12], "     *     ",ferry_104_e[13], "     *     ",ferry_104_e[14], "     *     ",ferry_104_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[16], "     *     ",ferry_104_e[17], "     *     ",ferry_104_e[18], "     *     ",ferry_104_e[19], "     *     ",ferry_104_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[21], "     *     ",ferry_104_e[22], "     *     ",ferry_104_e[23], "     *     ",ferry_104_e[24], "     *     ",ferry_104_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[26], "     *     ",ferry_104_e[27], "     *     ",ferry_104_e[28], "     *     ",ferry_104_e[29], "     *     ",ferry_104_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[31], "     *     ",ferry_104_e[32], "     *     ",ferry_104_e[33], "     *     ",ferry_104_e[34], "     *     ",ferry_104_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[36], "     *     ",ferry_104_e[37], "     *     ",ferry_104_e[38], "     *     ",ferry_104_e[39], "     *     ",ferry_104_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[41], "     *     ",ferry_104_e[42], "     *     ",ferry_104_e[43], "     *     ",ferry_104_e[44], "     *     ",ferry_104_e[45], "     *")
    print("***********************************************************************")



def ferryID_104():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 104                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_104_b[0], "     *     ",ferry_104_b[1], "     *     ",ferry_104_b[2], "     *     ",ferry_104_b[3], "     *     ",ferry_104_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_b[5], "     *     ",ferry_104_b[6], "     *     ",ferry_104_b[7], "     *     ",ferry_104_b[8], "     *     ",ferry_104_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[11], "     *     ",ferry_104_e[12], "     *     ",ferry_104_e[13], "     *     ",ferry_104_e[14], "     *     ",ferry_104_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[16], "     *     ",ferry_104_e[17], "     *     ",ferry_104_e[18], "     *     ",ferry_104_e[19], "     *     ",ferry_104_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[21], "     *     ",ferry_104_e[22], "     *     ",ferry_104_e[23], "     *     ",ferry_104_e[24], "     *     ",ferry_104_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[26], "     *     ",ferry_104_e[27], "     *     ",ferry_104_e[28], "     *     ",ferry_104_e[29], "     *     ",ferry_104_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[31], "     *     ",ferry_104_e[32], "     *     ",ferry_104_e[33], "     *     ",ferry_104_e[34], "     *     ",ferry_104_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[36], "     *     ",ferry_104_e[37], "     *     ",ferry_104_e[38], "     *     ",ferry_104_e[39], "     *     ",ferry_104_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[41], "     *     ",ferry_104_e[42], "     *     ",ferry_104_e[43], "     *     ",ferry_104_e[44], "     *     ",ferry_104_e[45], "     *")
    print("***********************************************************************")

#FerryID 5:
ferry_105_b = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
ferry_105_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_105_b():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 105                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_105_b[0], "     *     ",ferry_105_b[1], "     *     ",ferry_105_b[2], "     *     ",ferry_105_b[3], "     *     ",ferry_105_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_105_b[5], "     *     ",ferry_105_b[6], "     *     ",ferry_105_b[7], "     *     ",ferry_105_b[8], "     *     ",ferry_105_b[9], "     *")
    print("***********************************************************************")
def ferryID_105_e():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 105                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_105_e[11], "     *     ",ferry_105_e[12], "     *     ",ferry_105_e[13], "     *     ",ferry_105_e[14], "     *     ",ferry_105_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_105_e[16], "     *     ",ferry_105_e[17], "     *     ",ferry_105_e[18], "     *     ",ferry_105_e[19], "     *     ",ferry_105_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_105_e[21], "     *     ",ferry_105_e[22], "     *     ",ferry_105_e[23], "     *     ",ferry_105_e[24], "     *     ",ferry_105_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_105_e[26], "     *     ",ferry_105_e[27], "     *     ",ferry_105_e[28], "     *     ",ferry_105_e[29], "     *     ",ferry_105_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_105_e[31], "     *     ",ferry_105_e[32], "     *     ",ferry_105_e[33], "     *     ",ferry_105_e[34], "     *     ",ferry_105_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_105_e[36], "     *     ",ferry_105_e[37], "     *     ",ferry_105_e[38], "     *     ",ferry_105_e[39], "     *     ",ferry_105_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_105_e[41], "     *     ",ferry_105_e[42], "     *     ",ferry_105_e[43], "     *     ",ferry_105_e[44], "     *     ",ferry_105_e[45], "     *")
    print("***********************************************************************")



def ferryID_105():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 105                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_105_b[0], "     *     ",ferry_105_b[1], "     *     ",ferry_105_b[2], "     *     ",ferry_105_b[3], "     *     ",ferry_105_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_105_b[5], "     *     ",ferry_105_b[6], "     *     ",ferry_105_b[7], "     *     ",ferry_105_b[8], "     *     ",ferry_105_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_105_e[11], "     *     ",ferry_105_e[12], "     *     ",ferry_105_e[13], "     *     ",ferry_105_e[14], "     *     ",ferry_105_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_105_e[16], "     *     ",ferry_105_e[17], "     *     ",ferry_105_e[18], "     *     ",ferry_105_e[19], "     *     ",ferry_105_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_105_e[21], "     *     ",ferry_105_e[22], "     *     ",ferry_105_e[23], "     *     ",ferry_105_e[24], "     *     ",ferry_105_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_105_e[26], "     *     ",ferry_105_e[27], "     *     ",ferry_105_e[28], "     *     ",ferry_105_e[29], "     *     ",ferry_105_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_105_e[31], "     *     ",ferry_105_e[32], "     *     ",ferry_105_e[33], "     *     ",ferry_105_e[34], "     *     ",ferry_105_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_105_e[36], "     *     ",ferry_105_e[37], "     *     ",ferry_105_e[38], "     *     ",ferry_105_e[39], "     *     ",ferry_105_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_105_e[41], "     *     ",ferry_105_e[42], "     *     ",ferry_105_e[43], "     *     ",ferry_105_e[44], "     *     ",ferry_105_e[45], "     *")
    print("***********************************************************************")


#FerryID 6:
ferry_106_b = [1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
ferry_106_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_106_b():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 106                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_106_b[0], "     *     ",ferry_106_b[1], "     *     ",ferry_106_b[2], "     *     ",ferry_106_b[3], "     *     ",ferry_106_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_106_b[5], "     *     ",ferry_106_b[6], "     *     ",ferry_106_b[7], "     *     ",ferry_106_b[8], "     *     ",ferry_106_b[9], "     *")
    print("***********************************************************************")
def ferryID_106_e():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 106                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_106_e[11], "     *     ",ferry_106_e[12], "     *     ",ferry_106_e[13], "     *     ",ferry_106_e[14], "     *     ",ferry_106_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_106_e[16], "     *     ",ferry_106_e[17], "     *     ",ferry_106_e[18], "     *     ",ferry_106_e[19], "     *     ",ferry_106_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_106_e[21], "     *     ",ferry_106_e[22], "     *     ",ferry_106_e[23], "     *     ",ferry_106_e[24], "     *     ",ferry_106_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_106_e[26], "     *     ",ferry_106_e[27], "     *     ",ferry_106_e[28], "     *     ",ferry_106_e[29], "     *     ",ferry_106_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_106_e[31], "     *     ",ferry_106_e[32], "     *     ",ferry_106_e[33], "     *     ",ferry_106_e[34], "     *     ",ferry_106_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_106_e[36], "     *     ",ferry_106_e[37], "     *     ",ferry_106_e[38], "     *     ",ferry_106_e[39], "     *     ",ferry_106_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_106_e[41], "     *     ",ferry_106_e[42], "     *     ",ferry_106_e[43], "     *     ",ferry_106_e[44], "     *     ",ferry_106_e[45], "     *")
    print("***********************************************************************")



def ferryID_106():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 106                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_106_b[0], "     *     ",ferry_106_b[1], "     *     ",ferry_106_b[2], "     *     ",ferry_106_b[3], "     *     ",ferry_106_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_106_b[5], "     *     ",ferry_106_b[6], "     *     ",ferry_106_b[7], "     *     ",ferry_106_b[8], "     *     ",ferry_106_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_106_e[11], "     *     ",ferry_106_e[12], "     *     ",ferry_106_e[13], "     *     ",ferry_106_e[14], "     *     ",ferry_106_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_106_e[16], "     *     ",ferry_106_e[17], "     *     ",ferry_106_e[18], "     *     ",ferry_106_e[19], "     *     ",ferry_106_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_106_e[21], "     *     ",ferry_106_e[22], "     *     ",ferry_106_e[23], "     *     ",ferry_106_e[24], "     *     ",ferry_106_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_106_e[26], "     *     ",ferry_106_e[27], "     *     ",ferry_106_e[28], "     *     ",ferry_106_e[29], "     *     ",ferry_106_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_106_e[31], "     *     ",ferry_106_e[32], "     *     ",ferry_106_e[33], "     *     ",ferry_106_e[34], "     *     ",ferry_106_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_106_e[36], "     *     ",ferry_106_e[37], "     *     ",ferry_106_e[38], "     *     ",ferry_106_e[39], "     *     ",ferry_106_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_106_e[41], "     *     ",ferry_106_e[42], "     *     ",ferry_106_e[43], "     *     ",ferry_106_e[44], "     *     ",ferry_106_e[45], "     *")
    print("***********************************************************************")


#FerryID 7:
ferry_107_b = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
ferry_107_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_107_b():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 107                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_107_b[0], "     *     ",ferry_107_b[1], "     *     ",ferry_107_b[2], "     *     ",ferry_107_b[3], "     *     ",ferry_107_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_107_b[5], "     *     ",ferry_107_b[6], "     *     ",ferry_107_b[7], "     *     ",ferry_107_b[8], "     *     ",ferry_107_b[9], "     *")
    print("***********************************************************************")
def ferryID_107_e():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 107                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_107_e[11], "     *     ",ferry_107_e[12], "     *     ",ferry_107_e[13], "     *     ",ferry_107_e[14], "     *     ",ferry_107_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_107_e[16], "     *     ",ferry_107_e[17], "     *     ",ferry_107_e[18], "     *     ",ferry_107_e[19], "     *     ",ferry_107_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_107_e[21], "     *     ",ferry_107_e[22], "     *     ",ferry_107_e[23], "     *     ",ferry_107_e[24], "     *     ",ferry_107_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_107_e[26], "     *     ",ferry_107_e[27], "     *     ",ferry_107_e[28], "     *     ",ferry_107_e[29], "     *     ",ferry_107_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_107_e[31], "     *     ",ferry_107_e[32], "     *     ",ferry_107_e[33], "     *     ",ferry_107_e[34], "     *     ",ferry_107_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_107_e[36], "     *     ",ferry_107_e[37], "     *     ",ferry_107_e[38], "     *     ",ferry_107_e[39], "     *     ",ferry_107_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_107_e[41], "     *     ",ferry_107_e[42], "     *     ",ferry_107_e[43], "     *     ",ferry_107_e[44], "     *     ",ferry_107_e[45], "     *")
    print("***********************************************************************")




def ferryID_107():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 107                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_107_b[0], "     *     ",ferry_107_b[1], "     *     ",ferry_107_b[2], "     *     ",ferry_107_b[3], "     *     ",ferry_107_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_107_b[5], "     *     ",ferry_107_b[6], "     *     ",ferry_107_b[7], "     *     ",ferry_107_b[8], "     *     ",ferry_107_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_107_e[11], "     *     ",ferry_107_e[12], "     *     ",ferry_107_e[13], "     *     ",ferry_107_e[14], "     *     ",ferry_107_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_107_e[16], "     *     ",ferry_107_e[17], "     *     ",ferry_107_e[18], "     *     ",ferry_107_e[19], "     *     ",ferry_107_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_107_e[21], "     *     ",ferry_107_e[22], "     *     ",ferry_107_e[23], "     *     ",ferry_107_e[24], "     *     ",ferry_107_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_107_e[26], "     *     ",ferry_107_e[27], "     *     ",ferry_107_e[28], "     *     ",ferry_107_e[29], "     *     ",ferry_107_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_107_e[31], "     *     ",ferry_107_e[32], "     *     ",ferry_107_e[33], "     *     ",ferry_107_e[34], "     *     ",ferry_107_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_107_e[36], "     *     ",ferry_107_e[37], "     *     ",ferry_107_e[38], "     *     ",ferry_107_e[39], "     *     ",ferry_107_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_107_e[41], "     *     ",ferry_107_e[42], "     *     ",ferry_107_e[43], "     *     ",ferry_107_e[44], "     *     ",ferry_107_e[45], "     *")
    print("***********************************************************************")

#FerryID 8:
ferry_108_b = [1, 0, 1, 1, 0, 1, 0, 0, 0, 0]
ferry_108_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_108_b():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 108                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_108_b[0], "     *     ",ferry_108_b[1], "     *     ",ferry_108_b[2], "     *     ",ferry_108_b[3], "     *     ",ferry_108_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_108_b[5], "     *     ",ferry_108_b[6], "     *     ",ferry_108_b[7], "     *     ",ferry_108_b[8], "     *     ",ferry_108_b[9], "     *")
    print("***********************************************************************")
def ferryID_108_e():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 108                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_108_e[11], "     *     ",ferry_108_e[12], "     *     ",ferry_108_e[13], "     *     ",ferry_108_e[14], "     *     ",ferry_108_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_108_e[16], "     *     ",ferry_108_e[17], "     *     ",ferry_108_e[18], "     *     ",ferry_108_e[19], "     *     ",ferry_108_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_108_e[21], "     *     ",ferry_108_e[22], "     *     ",ferry_108_e[23], "     *     ",ferry_108_e[24], "     *     ",ferry_108_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_108_e[26], "     *     ",ferry_108_e[27], "     *     ",ferry_108_e[28], "     *     ",ferry_108_e[29], "     *     ",ferry_108_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_108_e[31], "     *     ",ferry_108_e[32], "     *     ",ferry_108_e[33], "     *     ",ferry_108_e[34], "     *     ",ferry_108_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_108_e[36], "     *     ",ferry_108_e[37], "     *     ",ferry_108_e[38], "     *     ",ferry_108_e[39], "     *     ",ferry_108_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_108_e[41], "     *     ",ferry_108_e[42], "     *     ",ferry_108_e[43], "     *     ",ferry_108_e[44], "     *     ",ferry_108_e[45], "     *")
    print("***********************************************************************")




def ferryID_108():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 108                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_108_b[0], "     *     ",ferry_108_b[1], "     *     ",ferry_108_b[2], "     *     ",ferry_108_b[3], "     *     ",ferry_108_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_108_b[5], "     *     ",ferry_108_b[6], "     *     ",ferry_108_b[7], "     *     ",ferry_108_b[8], "     *     ",ferry_108_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_108_e[11], "     *     ",ferry_108_e[12], "     *     ",ferry_108_e[13], "     *     ",ferry_108_e[14], "     *     ",ferry_108_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_108_e[16], "     *     ",ferry_108_e[17], "     *     ",ferry_108_e[18], "     *     ",ferry_108_e[19], "     *     ",ferry_108_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_108_e[21], "     *     ",ferry_108_e[22], "     *     ",ferry_108_e[23], "     *     ",ferry_108_e[24], "     *     ",ferry_108_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_108_e[26], "     *     ",ferry_108_e[27], "     *     ",ferry_108_e[28], "     *     ",ferry_108_e[29], "     *     ",ferry_108_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_108_e[31], "     *     ",ferry_108_e[32], "     *     ",ferry_108_e[33], "     *     ",ferry_108_e[34], "     *     ",ferry_108_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_108_e[36], "     *     ",ferry_108_e[37], "     *     ",ferry_108_e[38], "     *     ",ferry_108_e[39], "     *     ",ferry_108_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_108_e[41], "     *     ",ferry_108_e[42], "     *     ",ferry_108_e[43], "     *     ",ferry_108_e[44], "     *     ",ferry_108_e[45], "     *")
    print("***********************************************************************")






#----------------------FERRY ID FOR PENANG----------------------------
#FerryID 1:
ferry_201_b = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ferry_201_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_201_b():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 201                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_201_b[0], "     *     ",ferry_201_b[1], "     *     ",ferry_201_b[2], "     *     ",ferry_201_b[3], "     *     ",ferry_201_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_b[5], "     *     ",ferry_201_b[6], "     *     ",ferry_201_b[7], "     *     ",ferry_201_b[8], "     *     ",ferry_201_b[9], "     *")
    print("***********************************************************************")
def ferryID_201_e():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 201                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[11], "     *     ",ferry_201_e[12], "     *     ",ferry_201_e[13], "     *     ",ferry_201_e[14], "     *     ",ferry_201_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[16], "     *     ",ferry_201_e[17], "     *     ",ferry_201_e[18], "     *     ",ferry_201_e[19], "     *     ",ferry_201_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[21], "     *     ",ferry_201_e[22], "     *     ",ferry_201_e[23], "     *     ",ferry_201_e[24], "     *     ",ferry_201_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[26], "     *     ",ferry_201_e[27], "     *     ",ferry_201_e[28], "     *     ",ferry_201_e[29], "     *     ",ferry_201_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[31], "     *     ",ferry_201_e[32], "     *     ",ferry_201_e[33], "     *     ",ferry_201_e[34], "     *     ",ferry_201_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[36], "     *     ",ferry_201_e[37], "     *     ",ferry_201_e[38], "     *     ",ferry_201_e[39], "     *     ",ferry_201_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[41], "     *     ",ferry_201_e[42], "     *     ",ferry_201_e[43], "     *     ",ferry_201_e[44], "     *     ",ferry_201_e[45], "     *")
    print("***********************************************************************")


def ferryID_201():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 201                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_201_b[0], "     *     ",ferry_201_b[1], "     *     ",ferry_201_b[2], "     *     ",ferry_201_b[3], "     *     ",ferry_201_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_b[5], "     *     ",ferry_201_b[6], "     *     ",ferry_201_b[7], "     *     ",ferry_201_b[8], "     *     ",ferry_201_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[11], "     *     ",ferry_201_e[12], "     *     ",ferry_201_e[13], "     *     ",ferry_201_e[14], "     *     ",ferry_201_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[16], "     *     ",ferry_201_e[17], "     *     ",ferry_201_e[18], "     *     ",ferry_201_e[19], "     *     ",ferry_201_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[21], "     *     ",ferry_201_e[22], "     *     ",ferry_201_e[23], "     *     ",ferry_201_e[24], "     *     ",ferry_201_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[26], "     *     ",ferry_201_e[27], "     *     ",ferry_201_e[28], "     *     ",ferry_201_e[29], "     *     ",ferry_201_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[31], "     *     ",ferry_201_e[32], "     *     ",ferry_201_e[33], "     *     ",ferry_201_e[34], "     *     ",ferry_201_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[36], "     *     ",ferry_201_e[37], "     *     ",ferry_201_e[38], "     *     ",ferry_201_e[39], "     *     ",ferry_201_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[41], "     *     ",ferry_201_e[42], "     *     ",ferry_201_e[43], "     *     ",ferry_201_e[44], "     *     ",ferry_201_e[45], "     *")
    print("***********************************************************************")

#FerryID 2:
ferry_202_b = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
ferry_202_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_202_b():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 202                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_202_b[0], "     *     ",ferry_202_b[1], "     *     ",ferry_202_b[2], "     *     ",ferry_202_b[3], "     *     ",ferry_202_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_b[5], "     *     ",ferry_202_b[6], "     *     ",ferry_202_b[7], "     *     ",ferry_202_b[8], "     *     ",ferry_202_b[9], "     *")
    print("***********************************************************************")
def ferryID_202_e():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 202                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[11], "     *     ",ferry_202_e[12], "     *     ",ferry_202_e[13], "     *     ",ferry_202_e[14], "     *     ",ferry_202_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[16], "     *     ",ferry_202_e[17], "     *     ",ferry_202_e[18], "     *     ",ferry_202_e[19], "     *     ",ferry_202_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[21], "     *     ",ferry_202_e[22], "     *     ",ferry_202_e[23], "     *     ",ferry_202_e[24], "     *     ",ferry_202_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[26], "     *     ",ferry_202_e[27], "     *     ",ferry_202_e[28], "     *     ",ferry_202_e[29], "     *     ",ferry_202_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[31], "     *     ",ferry_202_e[32], "     *     ",ferry_202_e[33], "     *     ",ferry_202_e[34], "     *     ",ferry_202_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[36], "     *     ",ferry_202_e[37], "     *     ",ferry_202_e[38], "     *     ",ferry_202_e[39], "     *     ",ferry_202_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[41], "     *     ",ferry_202_e[42], "     *     ",ferry_202_e[43], "     *     ",ferry_202_e[44], "     *     ",ferry_202_e[45], "     *")
    print("***********************************************************************")


def ferryID_202():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 202                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_202_b[0], "     *     ",ferry_202_b[1], "     *     ",ferry_202_b[2], "     *     ",ferry_202_b[3], "     *     ",ferry_202_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_b[5], "     *     ",ferry_202_b[6], "     *     ",ferry_202_b[7], "     *     ",ferry_202_b[8], "     *     ",ferry_202_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[11], "     *     ",ferry_202_e[12], "     *     ",ferry_202_e[13], "     *     ",ferry_202_e[14], "     *     ",ferry_202_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[16], "     *     ",ferry_202_e[17], "     *     ",ferry_202_e[18], "     *     ",ferry_202_e[19], "     *     ",ferry_202_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[21], "     *     ",ferry_202_e[22], "     *     ",ferry_202_e[23], "     *     ",ferry_202_e[24], "     *     ",ferry_202_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[26], "     *     ",ferry_202_e[27], "     *     ",ferry_202_e[28], "     *     ",ferry_202_e[29], "     *     ",ferry_202_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[31], "     *     ",ferry_202_e[32], "     *     ",ferry_202_e[33], "     *     ",ferry_202_e[34], "     *     ",ferry_202_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[36], "     *     ",ferry_202_e[37], "     *     ",ferry_202_e[38], "     *     ",ferry_202_e[39], "     *     ",ferry_202_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[41], "     *     ",ferry_202_e[42], "     *     ",ferry_202_e[43], "     *     ",ferry_202_e[44], "     *     ",ferry_202_e[45], "     *")
    print("***********************************************************************")

#FerryID 3:
ferry_203_b = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
ferry_203_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_203_b():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 203                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_203_b[0], "     *     ",ferry_203_b[1], "     *     ",ferry_203_b[2], "     *     ",ferry_203_b[3], "     *     ",ferry_203_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_b[5], "     *     ",ferry_203_b[6], "     *     ",ferry_203_b[7], "     *     ",ferry_203_b[8], "     *     ",ferry_203_b[9], "     *")
    print("***********************************************************************")
def ferryID_203_e():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 203                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[11], "     *     ",ferry_203_e[12], "     *     ",ferry_203_e[13], "     *     ",ferry_203_e[14], "     *     ",ferry_203_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[16], "     *     ",ferry_203_e[17], "     *     ",ferry_203_e[18], "     *     ",ferry_203_e[19], "     *     ",ferry_203_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[21], "     *     ",ferry_203_e[22], "     *     ",ferry_203_e[23], "     *     ",ferry_203_e[24], "     *     ",ferry_203_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[26], "     *     ",ferry_203_e[27], "     *     ",ferry_203_e[28], "     *     ",ferry_203_e[29], "     *     ",ferry_203_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[31], "     *     ",ferry_203_e[32], "     *     ",ferry_203_e[33], "     *     ",ferry_203_e[34], "     *     ",ferry_203_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[36], "     *     ",ferry_203_e[37], "     *     ",ferry_203_e[38], "     *     ",ferry_203_e[39], "     *     ",ferry_203_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[41], "     *     ",ferry_203_e[42], "     *     ",ferry_203_e[43], "     *     ",ferry_203_e[44], "     *     ",ferry_203_e[45], "     *")
    print("***********************************************************************")


def ferryID_203():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 203                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_203_b[0], "     *     ",ferry_203_b[1], "     *     ",ferry_203_b[2], "     *     ",ferry_203_b[3], "     *     ",ferry_203_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_b[5], "     *     ",ferry_203_b[6], "     *     ",ferry_203_b[7], "     *     ",ferry_203_b[8], "     *     ",ferry_203_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[11], "     *     ",ferry_203_e[12], "     *     ",ferry_203_e[13], "     *     ",ferry_203_e[14], "     *     ",ferry_203_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[16], "     *     ",ferry_203_e[17], "     *     ",ferry_203_e[18], "     *     ",ferry_203_e[19], "     *     ",ferry_203_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[21], "     *     ",ferry_203_e[22], "     *     ",ferry_203_e[23], "     *     ",ferry_203_e[24], "     *     ",ferry_203_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[26], "     *     ",ferry_203_e[27], "     *     ",ferry_203_e[28], "     *     ",ferry_203_e[29], "     *     ",ferry_203_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[31], "     *     ",ferry_203_e[32], "     *     ",ferry_203_e[33], "     *     ",ferry_203_e[34], "     *     ",ferry_203_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[36], "     *     ",ferry_203_e[37], "     *     ",ferry_203_e[38], "     *     ",ferry_203_e[39], "     *     ",ferry_203_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[41], "     *     ",ferry_203_e[42], "     *     ",ferry_203_e[43], "     *     ",ferry_203_e[44], "     *     ",ferry_203_e[45], "     *")
    print("***********************************************************************")

#FerryID 4:
ferry_204_b = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
ferry_204_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_204_b():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 204                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_204_b[0], "     *     ",ferry_204_b[1], "     *     ",ferry_204_b[2], "     *     ",ferry_204_b[3], "     *     ",ferry_204_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_b[5], "     *     ",ferry_204_b[6], "     *     ",ferry_204_b[7], "     *     ",ferry_204_b[8], "     *     ",ferry_204_b[9], "     *")
    print("***********************************************************************")
def ferryID_204_e():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 204                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[11], "     *     ",ferry_204_e[12], "     *     ",ferry_204_e[13], "     *     ",ferry_204_e[14], "     *     ",ferry_204_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[16], "     *     ",ferry_204_e[17], "     *     ",ferry_204_e[18], "     *     ",ferry_204_e[19], "     *     ",ferry_204_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[21], "     *     ",ferry_204_e[22], "     *     ",ferry_204_e[23], "     *     ",ferry_204_e[24], "     *     ",ferry_204_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[26], "     *     ",ferry_204_e[27], "     *     ",ferry_204_e[28], "     *     ",ferry_204_e[29], "     *     ",ferry_204_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[31], "     *     ",ferry_204_e[32], "     *     ",ferry_204_e[33], "     *     ",ferry_204_e[34], "     *     ",ferry_204_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[36], "     *     ",ferry_204_e[37], "     *     ",ferry_204_e[38], "     *     ",ferry_204_e[39], "     *     ",ferry_204_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[41], "     *     ",ferry_204_e[42], "     *     ",ferry_204_e[43], "     *     ",ferry_204_e[44], "     *     ",ferry_204_e[45], "     *")
    print("***********************************************************************")


def ferryID_204():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 204                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_204_b[0], "     *     ",ferry_204_b[1], "     *     ",ferry_204_b[2], "     *     ",ferry_204_b[3], "     *     ",ferry_204_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_b[5], "     *     ",ferry_204_b[6], "     *     ",ferry_204_b[7], "     *     ",ferry_204_b[8], "     *     ",ferry_204_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[11], "     *     ",ferry_204_e[12], "     *     ",ferry_204_e[13], "     *     ",ferry_204_e[14], "     *     ",ferry_204_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[16], "     *     ",ferry_204_e[17], "     *     ",ferry_204_e[18], "     *     ",ferry_204_e[19], "     *     ",ferry_204_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[21], "     *     ",ferry_204_e[22], "     *     ",ferry_204_e[23], "     *     ",ferry_204_e[24], "     *     ",ferry_204_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[26], "     *     ",ferry_204_e[27], "     *     ",ferry_204_e[28], "     *     ",ferry_204_e[29], "     *     ",ferry_204_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[31], "     *     ",ferry_204_e[32], "     *     ",ferry_204_e[33], "     *     ",ferry_204_e[34], "     *     ",ferry_204_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[36], "     *     ",ferry_204_e[37], "     *     ",ferry_204_e[38], "     *     ",ferry_204_e[39], "     *     ",ferry_204_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[41], "     *     ",ferry_204_e[42], "     *     ",ferry_204_e[43], "     *     ",ferry_204_e[44], "     *     ",ferry_204_e[45], "     *")
    print("***********************************************************************")


#FerryID 5:
ferry_205_b = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
ferry_205_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_205_b():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 205                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_205_b[0], "     *     ",ferry_205_b[1], "     *     ",ferry_205_b[2], "     *     ",ferry_205_b[3], "     *     ",ferry_205_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_205_b[5], "     *     ",ferry_205_b[6], "     *     ",ferry_205_b[7], "     *     ",ferry_205_b[8], "     *     ",ferry_205_b[9], "     *")
    print("***********************************************************************")
def ferryID_205_e():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 205                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_205_e[11], "     *     ",ferry_205_e[12], "     *     ",ferry_205_e[13], "     *     ",ferry_205_e[14], "     *     ",ferry_205_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_205_e[16], "     *     ",ferry_205_e[17], "     *     ",ferry_205_e[18], "     *     ",ferry_205_e[19], "     *     ",ferry_205_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_205_e[21], "     *     ",ferry_205_e[22], "     *     ",ferry_205_e[23], "     *     ",ferry_205_e[24], "     *     ",ferry_205_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_205_e[26], "     *     ",ferry_205_e[27], "     *     ",ferry_205_e[28], "     *     ",ferry_205_e[29], "     *     ",ferry_205_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_205_e[31], "     *     ",ferry_205_e[32], "     *     ",ferry_205_e[33], "     *     ",ferry_205_e[34], "     *     ",ferry_205_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_205_e[36], "     *     ",ferry_205_e[37], "     *     ",ferry_205_e[38], "     *     ",ferry_205_e[39], "     *     ",ferry_205_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_205_e[41], "     *     ",ferry_205_e[42], "     *     ",ferry_205_e[43], "     *     ",ferry_205_e[44], "     *     ",ferry_205_e[45], "     *")
    print("***********************************************************************")

def ferryID_205():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 205                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_205_b[0], "     *     ",ferry_205_b[1], "     *     ",ferry_205_b[2], "     *     ",ferry_205_b[3], "     *     ",ferry_205_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_205_b[5], "     *     ",ferry_205_b[6], "     *     ",ferry_205_b[7], "     *     ",ferry_205_b[8], "     *     ",ferry_205_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_205_e[11], "     *     ",ferry_205_e[12], "     *     ",ferry_205_e[13], "     *     ",ferry_205_e[14], "     *     ",ferry_205_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_205_e[16], "     *     ",ferry_205_e[17], "     *     ",ferry_205_e[18], "     *     ",ferry_205_e[19], "     *     ",ferry_205_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_205_e[21], "     *     ",ferry_205_e[22], "     *     ",ferry_205_e[23], "     *     ",ferry_205_e[24], "     *     ",ferry_205_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_205_e[26], "     *     ",ferry_205_e[27], "     *     ",ferry_205_e[28], "     *     ",ferry_205_e[29], "     *     ",ferry_205_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_205_e[31], "     *     ",ferry_205_e[32], "     *     ",ferry_205_e[33], "     *     ",ferry_205_e[34], "     *     ",ferry_205_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_205_e[36], "     *     ",ferry_205_e[37], "     *     ",ferry_205_e[38], "     *     ",ferry_205_e[39], "     *     ",ferry_205_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_205_e[41], "     *     ",ferry_205_e[42], "     *     ",ferry_205_e[43], "     *     ",ferry_205_e[44], "     *     ",ferry_205_e[45], "     *")
    print("***********************************************************************")

#FerryID 6:
ferry_206_b = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
ferry_206_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_206_b():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 206                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_206_b[0], "     *     ",ferry_206_b[1], "     *     ",ferry_206_b[2], "     *     ",ferry_206_b[3], "     *     ",ferry_206_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_206_b[5], "     *     ",ferry_206_b[6], "     *     ",ferry_206_b[7], "     *     ",ferry_206_b[8], "     *     ",ferry_206_b[9], "     *")
    print("***********************************************************************")
def ferryID_206_e():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 206                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_206_e[11], "     *     ",ferry_206_e[12], "     *     ",ferry_206_e[13], "     *     ",ferry_206_e[14], "     *     ",ferry_206_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_206_e[16], "     *     ",ferry_206_e[17], "     *     ",ferry_206_e[18], "     *     ",ferry_206_e[19], "     *     ",ferry_206_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_206_e[21], "     *     ",ferry_206_e[22], "     *     ",ferry_206_e[23], "     *     ",ferry_206_e[24], "     *     ",ferry_206_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_206_e[26], "     *     ",ferry_206_e[27], "     *     ",ferry_206_e[28], "     *     ",ferry_206_e[29], "     *     ",ferry_206_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_206_e[31], "     *     ",ferry_206_e[32], "     *     ",ferry_206_e[33], "     *     ",ferry_206_e[34], "     *     ",ferry_206_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_206_e[36], "     *     ",ferry_206_e[37], "     *     ",ferry_206_e[38], "     *     ",ferry_206_e[39], "     *     ",ferry_206_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_206_e[41], "     *     ",ferry_206_e[42], "     *     ",ferry_206_e[43], "     *     ",ferry_206_e[44], "     *     ",ferry_206_e[45], "     *")
    print("***********************************************************************")


def ferryID_206():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 206                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_206_b[0], "     *     ",ferry_206_b[1], "     *     ",ferry_206_b[2], "     *     ",ferry_206_b[3], "     *     ",ferry_206_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_206_b[5], "     *     ",ferry_206_b[6], "     *     ",ferry_206_b[7], "     *     ",ferry_206_b[8], "     *     ",ferry_206_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_206_e[11], "     *     ",ferry_206_e[12], "     *     ",ferry_206_e[13], "     *     ",ferry_206_e[14], "     *     ",ferry_206_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_206_e[16], "     *     ",ferry_206_e[17], "     *     ",ferry_206_e[18], "     *     ",ferry_206_e[19], "     *     ",ferry_206_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_206_e[21], "     *     ",ferry_206_e[22], "     *     ",ferry_206_e[23], "     *     ",ferry_206_e[24], "     *     ",ferry_206_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_206_e[26], "     *     ",ferry_206_e[27], "     *     ",ferry_206_e[28], "     *     ",ferry_206_e[29], "     *     ",ferry_206_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_206_e[31], "     *     ",ferry_206_e[32], "     *     ",ferry_206_e[33], "     *     ",ferry_206_e[34], "     *     ",ferry_206_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_206_e[36], "     *     ",ferry_206_e[37], "     *     ",ferry_206_e[38], "     *     ",ferry_206_e[39], "     *     ",ferry_206_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_206_e[41], "     *     ",ferry_206_e[42], "     *     ",ferry_206_e[43], "     *     ",ferry_206_e[44], "     *     ",ferry_206_e[45], "     *")
    print("***********************************************************************")

#FerryID 7:
ferry_207_b = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
ferry_207_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_207_b():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 207                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_207_b[0], "     *     ",ferry_207_b[1], "     *     ",ferry_207_b[2], "     *     ",ferry_207_b[3], "     *     ",ferry_207_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_207_b[5], "     *     ",ferry_207_b[6], "     *     ",ferry_207_b[7], "     *     ",ferry_207_b[8], "     *     ",ferry_207_b[9], "     *")
    print("***********************************************************************")
def ferryID_207_e():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 207                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_207_e[11], "     *     ",ferry_207_e[12], "     *     ",ferry_207_e[13], "     *     ",ferry_207_e[14], "     *     ",ferry_207_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_207_e[16], "     *     ",ferry_207_e[17], "     *     ",ferry_207_e[18], "     *     ",ferry_207_e[19], "     *     ",ferry_207_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_207_e[21], "     *     ",ferry_207_e[22], "     *     ",ferry_207_e[23], "     *     ",ferry_207_e[24], "     *     ",ferry_207_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_207_e[26], "     *     ",ferry_207_e[27], "     *     ",ferry_207_e[28], "     *     ",ferry_207_e[29], "     *     ",ferry_207_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_207_e[31], "     *     ",ferry_207_e[32], "     *     ",ferry_207_e[33], "     *     ",ferry_207_e[34], "     *     ",ferry_207_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_207_e[36], "     *     ",ferry_207_e[37], "     *     ",ferry_207_e[38], "     *     ",ferry_207_e[39], "     *     ",ferry_207_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_207_e[41], "     *     ",ferry_207_e[42], "     *     ",ferry_207_e[43], "     *     ",ferry_207_e[44], "     *     ",ferry_207_e[45], "     *")
    print("***********************************************************************")


def ferryID_207():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 207                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_207_b[0], "     *     ",ferry_207_b[1], "     *     ",ferry_207_b[2], "     *     ",ferry_207_b[3], "     *     ",ferry_207_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_207_b[5], "     *     ",ferry_207_b[6], "     *     ",ferry_207_b[7], "     *     ",ferry_207_b[8], "     *     ",ferry_207_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_207_e[11], "     *     ",ferry_207_e[12], "     *     ",ferry_207_e[13], "     *     ",ferry_207_e[14], "     *     ",ferry_207_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_207_e[16], "     *     ",ferry_207_e[17], "     *     ",ferry_207_e[18], "     *     ",ferry_207_e[19], "     *     ",ferry_207_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_207_e[21], "     *     ",ferry_207_e[22], "     *     ",ferry_207_e[23], "     *     ",ferry_207_e[24], "     *     ",ferry_207_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_207_e[26], "     *     ",ferry_207_e[27], "     *     ",ferry_207_e[28], "     *     ",ferry_207_e[29], "     *     ",ferry_207_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_207_e[31], "     *     ",ferry_207_e[32], "     *     ",ferry_207_e[33], "     *     ",ferry_207_e[34], "     *     ",ferry_207_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_207_e[36], "     *     ",ferry_207_e[37], "     *     ",ferry_207_e[38], "     *     ",ferry_207_e[39], "     *     ",ferry_207_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_207_e[41], "     *     ",ferry_207_e[42], "     *     ",ferry_207_e[43], "     *     ",ferry_207_e[44], "     *     ",ferry_207_e[45], "     *")
    print("***********************************************************************")

#FerryID 8:
ferry_208_b = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
ferry_208_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_208_b():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 208                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_208_b[0], "     *     ",ferry_208_b[1], "     *     ",ferry_208_b[2], "     *     ",ferry_208_b[3], "     *     ",ferry_208_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_208_b[5], "     *     ",ferry_208_b[6], "     *     ",ferry_208_b[7], "     *     ",ferry_208_b[8], "     *     ",ferry_208_b[9], "     *")
    print("***********************************************************************")
def ferryID_208_e():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 208                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_208_e[11], "     *     ",ferry_208_e[12], "     *     ",ferry_208_e[13], "     *     ",ferry_208_e[14], "     *     ",ferry_208_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_208_e[16], "     *     ",ferry_208_e[17], "     *     ",ferry_208_e[18], "     *     ",ferry_208_e[19], "     *     ",ferry_208_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_208_e[21], "     *     ",ferry_208_e[22], "     *     ",ferry_208_e[23], "     *     ",ferry_208_e[24], "     *     ",ferry_208_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_208_e[26], "     *     ",ferry_208_e[27], "     *     ",ferry_208_e[28], "     *     ",ferry_208_e[29], "     *     ",ferry_208_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_208_e[31], "     *     ",ferry_208_e[32], "     *     ",ferry_208_e[33], "     *     ",ferry_208_e[34], "     *     ",ferry_208_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_208_e[36], "     *     ",ferry_208_e[37], "     *     ",ferry_208_e[38], "     *     ",ferry_208_e[39], "     *     ",ferry_208_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_208_e[41], "     *     ",ferry_208_e[42], "     *     ",ferry_208_e[43], "     *     ",ferry_208_e[44], "     *     ",ferry_208_e[45], "     *")
    print("***********************************************************************")


def ferryID_208():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 208                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_208_b[0], "     *     ",ferry_208_b[1], "     *     ",ferry_208_b[2], "     *     ",ferry_208_b[3], "     *     ",ferry_208_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_208_b[5], "     *     ",ferry_208_b[6], "     *     ",ferry_208_b[7], "     *     ",ferry_208_b[8], "     *     ",ferry_208_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_208_e[11], "     *     ",ferry_208_e[12], "     *     ",ferry_208_e[13], "     *     ",ferry_208_e[14], "     *     ",ferry_208_e[15], "     *")
    print("***********************************************************************")
    print("*     ",ferry_208_e[16], "     *     ",ferry_208_e[17], "     *     ",ferry_208_e[18], "     *     ",ferry_208_e[19], "     *     ",ferry_208_e[20], "     *")
    print("***********************************************************************")
    print("*     ",ferry_208_e[21], "     *     ",ferry_208_e[22], "     *     ",ferry_208_e[23], "     *     ",ferry_208_e[24], "     *     ",ferry_208_e[25], "     *")
    print("***********************************************************************")
    print("*     ",ferry_208_e[26], "     *     ",ferry_208_e[27], "     *     ",ferry_208_e[28], "     *     ",ferry_208_e[29], "     *     ",ferry_208_e[30], "     *")
    print("***********************************************************************")
    print("*     ",ferry_208_e[31], "     *     ",ferry_208_e[32], "     *     ",ferry_208_e[33], "     *     ",ferry_208_e[34], "     *     ",ferry_208_e[35], "     *")
    print("***********************************************************************")
    print("*     ",ferry_208_e[36], "     *     ",ferry_208_e[37], "     *     ",ferry_208_e[38], "     *     ",ferry_208_e[39], "     *     ",ferry_208_e[40], "     *")
    print("***********************************************************************")
    print("*     ",ferry_208_e[41], "     *     ",ferry_208_e[42], "     *     ",ferry_208_e[43], "     *     ",ferry_208_e[44], "     *     ",ferry_208_e[45], "     *")
    print("***********************************************************************")

main_menu()
