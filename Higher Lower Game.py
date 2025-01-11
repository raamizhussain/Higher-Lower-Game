import random

data = [
    {'name': 'Instagram', 'follower_count': 684, 'description': 'Social Media Platform', 'country': 'United States'},
    {'name': 'Cristiano Ronaldo', 'follower_count': 646, 'description': 'Footballer', 'country': 'Portugal'},
    {'name': 'Lionel Messi', 'follower_count': 504, 'description': 'Footballer', 'country': 'Argentina'},
    {'name': 'Selena Gomez', 'follower_count': 423, 'description': 'Musician and Actress', 'country': 'United States'},
    {'name': 'Kylie Jenner', 'follower_count': 395, 'description': 'Reality TV Star and Businesswoman', 'country': 'United States'},
    {'name': 'Dwayne Johnson', 'follower_count': 394, 'description': 'Actor and Professional Wrestler', 'country': 'United States'},
    {'name': 'Ariana Grande', 'follower_count': 376, 'description': 'Musician and Actress', 'country': 'United States'},
    {'name': 'Kim Kardashian', 'follower_count': 359, 'description': 'Reality TV Star and Businesswoman', 'country': 'United States'},
    {'name': 'Beyoncé', 'follower_count': 313, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Khloé Kardashian', 'follower_count': 305, 'description': 'Reality TV Star and Businesswoman', 'country': 'United States'},
    {'name': 'Nike', 'follower_count': 302, 'description': 'Sports Brand', 'country': 'United States'},
    {'name': 'Justin Bieber', 'follower_count': 295, 'description': 'Musician', 'country': 'Canada'},
    {'name': 'Kendall Jenner', 'follower_count': 290, 'description': 'Model and Reality TV Star', 'country': 'United States'},
    {'name': 'Taylor Swift', 'follower_count': 283, 'description': 'Musician', 'country': 'United States'},
    {'name': 'National Geographic', 'follower_count': 280, 'description': 'Media Organization', 'country': 'United States'},
    {'name': 'Virat Kohli', 'follower_count': 270, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Jennifer Lopez', 'follower_count': 249, 'description': 'Musician and Actress', 'country': 'United States'},
    {'name': 'Nicki Minaj', 'follower_count': 227, 'description': 'Musician', 'country': 'Trinidad and Tobago'},
    {'name': 'Neymar', 'follower_count': 227, 'description': 'Footballer', 'country': 'Brazil'},
    {'name': 'Kourtney Kardashian', 'follower_count': 220, 'description': 'Reality TV Star and Businesswoman', 'country': 'United States'},
    {'name': 'Miley Cyrus', 'follower_count': 213, 'description': 'Musician and Actress', 'country': 'United States'},
    {'name': 'Katy Perry', 'follower_count': 205, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Zendaya', 'follower_count': 180, 'description': 'Actress and Singer', 'country': 'United States'},
    {'name': 'Kevin Hart', 'follower_count': 177, 'description': 'Comedian and Actor', 'country': 'United States'},
    {'name': 'Real Madrid CF', 'follower_count': 170, 'description': 'Football Club', 'country': 'Spain'},
    {'name': 'Cardi B', 'follower_count': 164, 'description': 'Musician and Rapper', 'country': 'United States'},
    {'name': 'LeBron James', 'follower_count': 159, 'description': 'Basketball Player', 'country': 'United States'},
    {'name': 'Demi Lovato', 'follower_count': 154, 'description': 'Musician and Actress', 'country': 'United States'},
    {'name': 'Rihanna', 'follower_count': 150, 'description': 'Musician and Businesswoman', 'country': 'Barbados'},
    {'name': 'Chris Brown', 'follower_count': 144, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Drake', 'follower_count': 143, 'description': 'Musician and Rapper', 'country': 'Canada'},
    {'name': 'Ellen DeGeneres', 'follower_count': 137, 'description': 'TV Host and Comedian', 'country': 'United States'},
    {'name': 'FC Barcelona', 'follower_count': 133, 'description': 'Football Club', 'country': 'Spain'},
    {'name': 'Kylian Mbappé', 'follower_count': 122, 'description': 'Footballer', 'country': 'France'},
    {'name': 'Billie Eilish', 'follower_count': 121, 'description': 'Musician', 'country': 'United States'},
    {'name': 'UEFA Champions League', 'follower_count': 118, 'description': 'Football Organization', 'country': 'Europe'},
    {'name': 'Gal Gadot', 'follower_count': 108, 'description': 'Actress', 'country': 'Israel'},
    {'name': 'Lisa', 'follower_count': 105, 'description': 'Musician (BLACKPINK)', 'country': 'Thailand'},
    {'name': 'Vin Diesel', 'follower_count': 103, 'description': 'Actor', 'country': 'United States'},
    {'name': 'NASA', 'follower_count': 96.9, 'description': 'Space Organization', 'country': 'United States'},
    {'name': 'Shraddha Kapoor', 'follower_count': 94.3, 'description': 'Actress', 'country': 'India'},
    {'name': 'Priyanka Chopra', 'follower_count': 92.6, 'description': 'Actress', 'country': 'India'},
    {'name': 'Narendra Modi', 'follower_count': 92.2, 'description': 'Prime Minister of India', 'country': 'India'},
    {'name': 'Shakira', 'follower_count': 90.8, 'description': 'Musician', 'country': 'Colombia'},
    {'name': 'NBA', 'follower_count': 89.2, 'description': 'Basketball Organization', 'country': 'United States'},
    {'name': 'Snoop Dogg', 'follower_count': 88.7, 'description': 'Musician and Rapper', 'country': 'United States'},
    {'name': 'David Beckham', 'follower_count': 88.3, 'description': 'Footballer', 'country': 'United Kingdom'},
    {'name': 'Dua Lipa', 'follower_count': 87.4, 'description': 'Musician', 'country': 'United Kingdom'},
    {'name': 'Alia Bhatt', 'follower_count': 86.1, 'description': 'Actress', 'country': 'India'},
    {'name': 'Jennie', 'follower_count': 85.9, 'description': 'Musician (BLACKPINK)', 'country': 'South Korea'}

]


account_a = random.choice(data)
account_b = random.choice(data)

while account_a == account_b:
    account_b = random.choice(data)
    
status = True    
score = 0
while status == True:
    print(f"Compare A: {account_a['name']} , a {account_a['description']}, from {account_a['country']}")
    print("\nVS\n")
    print(f"Against B: {account_b['name']} , a {account_b['description']}, from {account_b['country']}\n ")
    
    guess = input("Who has more followers (A or B): ").upper()
    if guess == "A":
        if account_a['follower_count'] < account_b['follower_count']:
            print(f"You Lose. Your score = {score}")
            status = False
        else:
            score += 1
            account_a = account_b
            account_b = random.choice(data)
            while account_a == account_b:
                account_b = random.choice(data)
            print(f"Your score: {score}")
    elif guess == "B":
        if account_a['follower_count'] > account_b['follower_count']:
            print(f"You Lose. Your score = {score}")
            status = False
        else:
            score += 1
            account_a = account_b
            account_b = random.choice(data)
            while account_a == account_b:
                account_b = random.choice(data)
            print(f"Your score: {score}")
    else:
        print("Enter valid input!")
    
    
    