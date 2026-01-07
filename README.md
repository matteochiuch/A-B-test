# An A/B test to see if the average of ratings for the highly discounted products is actually better than the average for the other products

I didn't do much analysis, just to see that the column was complete. then I proceed to define the 2 group based on the median value of the discount and then I have found the average ratings for each group. 
The absolute numbers are quite similar as the 2 groups have an average rating of 4.07 and 4.13 respectively withh variances of 0.071 and 0.096. 

### So can we say that the ratings for the products with bigger discount are actually better?

Yes, we can. Altough the two averages are quite close, I performed a Welch test and the reasults suggest that with 95% probability the average rating differ to each other, so people who get a greater discount on their online purchases usually show a greater satisfaction for their products.

Finally, it is also important to consider that almost 80% of the ratings are between 3.9 and 4.4, so if we contestualize the ratings like this the small difference of 0.06 between the 2 average actually looks quite more relevant. In other words a 6 point difference on a 400 points scale (from 1.00 to 5.00) looks actually irrilevant, while the same 6 points difference in a range of only 50 points (from 3.90 to 4.40) appears quite more important
