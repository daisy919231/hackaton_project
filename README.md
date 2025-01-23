1. One of the serious problems I had in the project was Integrity error, unique constraint failed. And I got this solved by changing my model User which was inheriting from EmailAbstactUser.
So the problem was in the EmailAbstractUser it already had EmailField() and I also had it in my customizing User model. Honestly, if haven't already made the model and 
then decided to inherit from a model, I probably would not have missed this fault. But, Alhamdullilah, the bug got fixed!
2. The second problem was database migration  problem. I dumped the data before switching from dbsqlite3 to postgresql and it kept inheriting integrity error and this time contenttypes
 already exists problem. I got it solved by not loading from a problematic json file and it worked.
                                                                                                        By Shahzoda
THIS IS FOR NOW!
