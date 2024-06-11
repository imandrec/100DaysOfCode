class Solution:
    def romanToInt(self, s: str) -> int:

        replacements = {
        'I' : '1',
        'V' : '5',
        'X' : '10',
        'L' : '50',
        'C' : '100',
        'D' : '500',
        'M' : '1000'}

        for key,value in replacements.items():
            s = s.replace(key,value)
        
        suma = sum(int(number) for number in s)
        return suma

        
