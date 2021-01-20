import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        city = input("Write a city name: Chicago, New York City or Washington? Don't worry about upper/lower cases").lower()
        if city not in CITY_DATA:
            print("\nThe answer is not correct.\n")
            continue   
        else:
            break

    while True:
        time = input("Do you want to filter data by month, by day, by all or by none?").lower()               
        
        if time == 'month':
            month = input("Which month you'd like to filter by? January, Feburary, March, April, May or June?").lower()
            day = 'all'
            break
                    
        elif time == 'day':
            month = 'all'
            day = input("Which day you'd like to filter by? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?").lower()
            break
                    
        elif time == 'all':
            month = input("Which month? January, Feburary, March, April, May or June?").lower()           
            day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?").lower()
            break       
        
        elif time == 'none':
            month = 'all'
            day = 'all'
            break       
        
        else:
            print("The chosen option is not available! Please try again: month, day, all or none?")
            continue

    print (city)
    print (month)
    print (day)
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    winner_month = df['month'].mode()[0]
    print (winner_month)

    # display the most common day of week
    winner_day = df['day_of_week'].mode()[0]
    print (winner_day)

    # display the most common start hour
    winner_hour = df['hour'].mode()[0]
    print (winner_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    winner_start = df['Start Station'].mode()[0]
    print(winner_start)

    # display most commonly used end station
    winner_end = df['End Station'].mode()[0]
    print(winner_end)

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    winner_combination = df['combination'].mode()[0]
    print(winner_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print(total_time)

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print(mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("There is no gender information here.")

    # Display earliest, most recent, and most common year of birth

    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print(earliest)
        latest = df['Birth_Year'].max()
        print(latest)
        winner_year = df['Birth Year'].mode()[0]
        print(winner_year)
    else:
        print("There is no birth year information here.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


"""Asking 5 lines of the raw data and more, if they want"""

def display_data(df):
    raw_data = 0
    while True:
        view_data = input("Do you want to see the raw data? Yes or No").lower()
        if view_data not in ['yes', 'no']:
            view_data = input("You wrote the wrong word. Please type Yes or No.").lower()
        elif view_data == 'yes':
            raw_data += 5
            print(df.iloc[raw_data : raw_data + 5])
            again = input("Do you want to see more? Yes or No").lower()
            if again == 'no':
                break
        elif view_data == 'no':
            return
  

def main():
    city = ""
    month = ""
    day = ""
    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data (df)

        restart = input('\nWould you like to restart? Enter yes or no, please.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
