from timelock import timelock_unlock_master_key

puzzle = input("Enter puzzle: ")
key = input("Enter master key: ")

msg = timelock_unlock_master_key(puzzle, key)
print(msg)
