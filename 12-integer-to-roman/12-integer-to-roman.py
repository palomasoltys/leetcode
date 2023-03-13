class Solution:
    def intToRoman(self, num: int) -> str:
        
        roman_symbols = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100], ["XC", 90], ["L", 50], ["XL", 40], ["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]
        
        roman_numeral = ""
        
        for sym, val in roman_symbols:
            count = num // val
            roman_numeral += (sym * count)
            num = num % val
            
        return roman_numeral
                
        