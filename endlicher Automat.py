# implement a simple finite automaton in Python
from typing import Dict


class State:
    def __init__(self, name: str, is_accepting: bool = False):
        self.name = name
        self.is_accepting = is_accepting
        self.transitions: Dict[str, 'State'] = {}

    def add_transition(self, symbol: str, state: 'State') -> None:
        self.transitions[symbol] = state

    def __str__(self) -> str:
        return f"State({self.name}, Accepting={self.is_accepting})"


class FiniteAutomaton:
    def __init__(self):
        self.states: Dict[str, State] = {}
        self.start_state: State = None

    def add_state(self, name: str, is_accepting: bool = False) -> State:
        state = State(name, is_accepting)
        self.states[name] = state
        if self.start_state is None:
            self.start_state = state
        return state

    def add_transition(self, from_state: str, to_state: str, symbol: str) -> None:
        if from_state in self.states and to_state in self.states:
            self.states[from_state].add_transition(symbol, self.states[to_state])

    def process_input(self, input_string: str) -> bool:
        current_state = self.start_state
        for symbol in input_string:
            if symbol in current_state.transitions:
                current_state = current_state.transitions[symbol]
            else:
                return False
        return current_state.is_accepting


# Example usage:
if __name__ == "__main__":
    fa = FiniteAutomaton()
    fa.add_state("q0", is_accepting=False)
    fa.add_state("q1", is_accepting=True)
    fa.add_transition("q0", "q1", "a")
    fa.add_transition("q1", "q0", "b")

    test_strings = ["a", "ab", "aba", "abab", "b", "aa"]
    for s in test_strings:
        result = fa.process_input(s)
        print(f"Input: {s}, Accepted: {result}")
