# PHASE-3-WK2-CodeChallenge
Authour:**Brian Mwangi Maina**

## Prerequisites:

**Technologies Used**

<li>Python

**Setup/Installation Requirements**

*To run the application, in your terminal*

<li>Open the terminal and clone the repository to your local machine: git clone git@github.com:BrwnBoy/PHASE-3-WK2-CodeChallenge.git//
<li>cd into *PHASE-3-WK2-CodeChallenge*
<li>Finally, open up vs.code by typing in (code .) while in the repository.

### How Do Each Of The Programs Run:

Through the use of several methods I gained functionality for instances of the class, Here are a few of them:

<li>*__init__*(self, name): This is the constructor method for the class. It's called when you create a new instance of the Restaurant class. The name parameter is the name of the restaurant. This name is stored in the instance variable _name.
<li>*name*(self): This is a property method that returns the name of the restaurant. The @property decorator makes it possible to access this method like an attribute, i.e., restaurant.name, instead of a method, i.e., restaurant.name().
<li>*reviews*(self): This method returns a list of all reviews for the restaurant. It does this by calling the all method on the Review class and filtering the results to only include reviews where review.restaurant is the same as the current restaurant instance (self).
<li>*customers*(self): This method returns a list of all unique customers who have left a review for the restaurant. It does this by calling the reviews method to get all reviews, then extracting the customer from each review. The set function is used to remove duplicates, and then it's converted back to a list.
<li>*average_star_rating*(self): This method calculates the average star rating for the restaurant. It does this by calling the reviews method to get all reviews, then extracting the rating from each review. The sum function is used to add up all the ratings, and then it's divided by the number of ratings to get the average. If there are no ratings, it returns 0.

**Please note that this code assumes the existence of a Review class with an all method, a restaurant attribute, a customer attribute, and a rating attribute. Without this class, the Restaurant class's reviews, customers, and average_star_rating methods will not work.**

#### License 

Copyright (c) 2023 Brian Mwangi Maina

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
