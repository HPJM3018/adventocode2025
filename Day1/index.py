position = 50
count = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if line: 
            direction = line[0]
            distance = int(line[1:])
            
            if direction == 'R':
                position = (position + distance) % 100
            else:  
                position = (position - distance) % 100
            
            if position == 0:
                count += 1

print(count)


###################################Part2##############################################################


position = 50
count = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if line:  
            direction = line[0]
            distance = int(line[1:])
            
            old_position = position
            
            if direction == 'R':
                position = (position + distance) % 100
                
                for step in range(1, distance + 1):
                    current_pos = (old_position + step) % 100
                    if current_pos == 0:
                        count += 1
            
            else: 
                position = (position - distance) % 100
                for step in range(1, distance + 1):
                    current_pos = (old_position - step) % 100
                    if current_pos == 0:
                        count += 1
print("partie 02 count")
print(count)