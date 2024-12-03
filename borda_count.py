num_candidates = int(input("Enter the number of candidates: "))
candidates = []
for i in range(num_candidates):
    name = input(f"Enter the name of candidate {i + 1}: ")
    candidates.append(name)
voters = int(input("Enter the number of voters: "))
def bordaCount(candidate, voters, name):
    ascii_art = r"""

  /$$$$$$$                            /$$                  /$$$$$$                                  /$$    
 | $$__  $$                          | $$                 /$$__  $$                                | $$    
 | $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$       | $$  \__/  /$$$$$$  /$$   /$$ /$$$$$$$  /$$$$$$  
 | $$$$$$$  /$$__  $$ /$$__  $$ /$$__  $$ |____  $$      | $$ /$$$$ /$$__  $$| $$  | $$| $$__  $$|_  $$_/  
 | $$__  $$| $$  \ $$| $$  \__/| $$  | $$  /$$$$$$$      | $$|_  $$| $$  \ $$| $$  | $$| $$  \ $$  | $$    
 | $$  \ $$| $$  | $$| $$      | $$  | $$ /$$__  $$      | $$  \ $$| $$  | $$| $$  | $$| $$  | $$  | $$ /$$
 | $$$$$$$/|  $$$$$$/| $$      |  $$$$$$$|  $$$$$$$      |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$  | $$  |  $$$$/
 |_______/  \______/ |__/       \_______/ \_______/       \______/  \______/  \______/ |__/  |__/   \___/  
                                                                                                          
"""
    print(ascii_art)

    votes = {candidate: 0 for candidate in candidates}
    for i in range(voters):
        print(f"Voter {i + 1}")
        print("Rank the candidates from 1 to", num_candidates, "(1 being the highest rank):")
        ranks = {}
        for candidate in candidates:
            rank = int(input(f"Rank for {candidate}: "))
            ranks[candidate] = rank
        for candidate, rank in ranks.items():
            if rank == num_candidates:
                votes[candidate] += 0
            else:
                votes[candidate] += (num_candidates - rank)
        sorted_results = sorted(votes.items(), key=lambda item: item[1], reverse=True)
        print("\nFinal ranking:")
        for rank, (name, score) in enumerate(sorted_results, start=1):
            print(f"{rank}. {name} with {score} points")

def plurality(candidates, voters, name):
    for i in range(voters):
        print("Pick a candidate:")
        for k in range(candidates):
            print(f"{k+1}. {candidates[k]}")
        # if k 

bordaCount(candidates, voters, name)