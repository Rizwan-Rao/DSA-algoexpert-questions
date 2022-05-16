Home_team_won = 1

def tournamentwinner(competitions,results):
    currentwinner=""
    scores={currentwinner:0}

    for idx,competition in enumerate(competitions):
        result=results[idx]
        home_team,away_team = competition
        winner_team = home_team if result==Home_team_won else away_team

        updatescores(winner_team,3,scores)

        if scores[winner_team]> scores[currentwinner]:
            currentwinner= winner_team
    return currentwinner

def updatescores(team,points,scores):
    if team not in scores:
        scores[team]=0
    scores[team]+=points
        

print(tournamentwinner([["html","c#"],["c#","python"],["python","html"]],[0,0,0]))        