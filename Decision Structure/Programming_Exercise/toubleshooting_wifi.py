#Using the flowchart to create the program.

print('Reboot the computer and try to connect.')
fix_problem = input('Did that fix the problem?')
if fix_problem == 'No':
    print('Reboot the router and try to connect')
    fix_problem = input('Did that fix the problem?')
    if fix_problem == 'No':
        print('Make sure the cables between the router and modem are plugged in firmly')
        fix_problem = input('Did that fix the problem?')
        if fix_problem == 'No':
            print('Move the router to a new location')            
            fix_problem = input('Did that fix the problem?')
            if fix_problem == 'No':
                print('Get a new router.')
            else:
                print('Problem fixed')
        else:
            print('Problem fixed.')
    else:
        print('Problem fixed')
else:
    print('Problem fixed')

