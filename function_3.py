#3. Date Parser
#Write a function which takes a list of datetime strings and converts it into a list of strings with only the date.

def date_parser(list_dates):
    #extract the date only : Courtney

    #append dates to new list : Mikael
    return 0

if __name__ == '__main__':
    dates = ['2019-11-29 12:50:54',
         '2019-11-29 12:46:53',
         '2019-11-29 12:46:10',
         '2019-11-29 12:33:36',
         '2019-11-29 12:17:43',
         '2019-11-29 11:28:40']
    print('date parser works : ',date_parser(dates) == ['2019-11-29','2019-11-29','2019-11-29','2019-11-29','2019-11-29','2019-11-29'])