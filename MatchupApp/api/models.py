from django.db import models
import string, random

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Match.objects.filter(code=code).count() == 0:
            break

    return code
# Create your models here.
class Match(models.Model):
    host = models.CharField(max_length=16, default="", unique=True)
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True)

    username = models.CharField(max_length=16, default="")
    tag = models.CharField(max_length=5, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    #start of User's account/game information/stats
    user_sumLevel = models.CharField(max_length=8, default = 0)
    user_role = models.CharField(max_length=8, default = 5)
    
    
    #start of User's Opponent account inormation/stats
    opp_username = models.CharField(max_length=16, default="")
    opp_tag = models.CharField(max_length=5, default="")
    opp_sumLevel = models.CharField(max_length=8, default = 0)
    opp_role = models.CharField(max_length=8, default = 5)

# Main Player
    #player stats

# Main Opponent
    #player stats

# Main Matchup
    #matchup info and blurbs