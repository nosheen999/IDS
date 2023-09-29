

# 29/09/2023
# CSC461 – Assignment2 – Regular Expressions
# Nosheen Azhar
# FA20-BSE-061
# In this task of regular expression we have given a text and we have to convert and exteract diffrent things from it according to the 10 question statement given in the assignment question papaer.


import re

# The text you provided
text = """
The outlook wasn't brillianb for the Mudville nine that day;
The score stood four to two, with but one inning more to play,
And then when Cooney died at first, and Barrows did the same,
A pall-like silence fell upon the patrons of the game.

A straggling few got up to go in deep despair. The rest
Clung to that hope which springs eternal in the human breast;
They thought, "If only Casey could but get a whack at that--
We'd put up even money now, with Casey at the bat."

But Flynn preceded Casey, as did also Jimmy Blake,
And the former was a lulu, while the latter was a cake;
So upon that stricken multitude grim melancholy sat,
For there seemed but little chance of Casey getting to the bat.

But Flynn let drive a single, to the wonderment of all,
And Blake, the much despised, tore the cover off the ball;
And when the dust had lifted, and men saw what had occurred,
There was Jimmy safe at second and Flynn a-hugging third.

Then from five thousand throats and more there rose a lusty yell;
It rumbled through the valley, it rattled in the dell;
It pounded on the mountain and recoiled upon the flat,
For Casey, mighty Casey, was advancing to the bat.

There was ease in Casey's manner as he stepped into his place;
There was pride in Casey's bearing and a smile lit Casey's face.
And when, responding to the cheers, he lightly doffed his hat,
No stranger in the crowd could doubt 'twas Casey at the bat.

Ten thousand eyes were on him as he rubbed his hands with dirt;
Five thousand tongues applauded when he wiped them on his shirt;
Then while the writhing pitcher ground the ball into his hip,
Defiance flashed in Casey's eye, a sneer curled Casey's lip.

And now the leather-covered sphere came hurtling through the air,
And Casey stood a-watching it in haughty grandeur there.
Close by the sturdy batsman the ball unheeded sped--
"That ain't my style," said Casey. "Strike one!" the umpire said.

From the benches, black with people, there went up a muffled roar,
Like the beating of the storm-waves on a stern and distant shore;
"Kill him! Kill the umpire!" shouted some one on the stand;
And it's likely they'd have killed him had not Casey raised his hand.

With a smile of Christian charity great Casey's visage shone;
He stilled the rising tumult; he bade the game go on;
He signaled to the pitcher, and once more the dun sphere flew;
But Casey still ignored it, and the umpire said, "Strike two!"

"Fraud!" cried the maddened thousands, and echo answered "Fraud!"
But one scornful look from Casey and the audience was awed.
They saw his face grow stern and cold, they saw his muscles strain,
And they knew that Casey wouldn't let that ball go by again.

The sneer has fled from Casey's lip, his teeth are clenched in hate;
He pounds with cruel violence his bat upon the plate.
And now the pitcher holds the ball, and now he lets it go.
And now the air is shattered by the force of Casey's blow.

Oh, somewhere in this favored land the sun is shining bright;
The band is playing somewhere, and somewhere hearts are light,
And somewhere men are laughing, and little children shout;
But there is no joy in Mudville--great Casey has struck out
"""

# Task 1: Extract list of all words
Task1 = re.findall(r'\b\w+\b', text)

# Task 2: Extract list of all words starting with a capital letter
Task2 = re.findall(r'\b[A-Z]\w*\b', text)

# Task 3: Extract list of all words of length 5
Task3 = re.findall(r'\b\w{5}\b', text)

# Task 4: Extract list of all words inside double quotes
Task4 = re.findall(r'"([^"]+)"', text)

# Task 5: Extract list of all vowels
Task5 = re.findall(r'[aeiouAEIOU]', text)

# Task 6: Extract list of 3 letter words ending with letter ‘e’
Task6 = re.findall(r'\b\w{2}e\b', text)

# Task 7: Extract list of all words starting and ending with letter ‘b’
Task7 = re.findall(r'\b[bB]\w*?b\b', text)

# Task 8: Remove all the punctuation marks from the text
Task8 = re.sub(r'[^\w\s]', '', text)
# Task 8: replace all n't with not
text9 = re.sub(r"n't\b", ' not', text)

# Task 10: Replace all new lines with a single space
Task10 = re.sub(r'\n', ' ', text)

# Print the results
print("Task 1: List of all words:", Task1)
print("\nTask 2: List of words starting with a capital letter:", Task2)
print("\nTask 3: List of words of length 5:", Task3)
print("\nTask 4: List of words inside double quotes:", Task4)
print("\nTask 5: List of vowels:", Task5)
print("\nTask 6: List of 3-letter words ending with 'e':", Task6)
print("\nTask 7: List of words starting and ending with 'b':", Task7)
print("\nTask 8: Text without punctuation marks:\n", Task8)
print("\nTask 9: Text with full forms of 'n't':\n", Task9)
print("\nTask 10: Text as a single line:\n", Task10)
