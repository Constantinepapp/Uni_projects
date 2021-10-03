class DFA:
    current_state = None
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
        return
    
    def transition_to_state_with_input(self, input_value):
        if ((self.current_state, input_value) not in self.transition_function.keys()):
            self.current_state = None
            return
        self.current_state = self.transition_function[(self.current_state, input_value)]
        return
    
    def in_accept_state(self):
        return self.current_state in accept_states
    
    def go_to_initial_state(self):
        self.current_state = self.start_state
        return
    
    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            continue
        return self.in_accept_state()
    pass


states = {-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
alphabet = {'(',')'}

tf = dict()


for i in range(-1,0):
    tf[(i,'(')] = i
    tf[(i,')')] = i
for i in range(0,20):
    tf[(i,'(')] = i+1
    tf[(i,')')] = i-1




start_state = 0

# η μονη επιτρεπτη τελικη κατασταση ειναι η 0
# αν η κατασταση παει -1 που σημαινει οτι σε καποιο σημειο του προγραμματος
# κλεισαν περισσοτερες παρενθεσεις απο οσες ειχαν ανοιξει και το προγραμμα τερματιζει 
# απο την αλλη ομως επιτρεπετε να ανοιξουν παραπανω απο μια παρενθεσεις χωρις να εχουν κλεισει
# αν στο τελος του προγραμματος δεν εχουν κλεισει οσες παρενθεσεις ανοιξαν το προγραμμα θα τερματισει με 
# state >0 η οποια δεν αποτελει αποδεκτη τερματικη κατασταση
accept_states = {0}

d = DFA(states, alphabet, tf, start_state, accept_states)


inp_program = [list('()'),list(')('),list('()('),list('())'),list('())('),list('()())))((('),list('()()((('),list('()()((()))')]

for input in inp_program:
    s=""
    print("input :",s.join(input))
    output = d.run_with_input_list(input)
    
    if output == True:
        print('Yes\n')
    else:
        print('No\n')