class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        
        self.words1to19 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

        self.words10to90 = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        self.scales = ['', 'Thousand', 'Million', 'Billion']
        
        word = ''
        scale = 0

        while num > 0:
            if num % 1000 != 0:
                word = self.convert(num % 1000) + self.scales[scale] + ' ' + word

            num //= 1000
            scale += 1
        
        return word.strip()
    
    def convert(self, num):
        if num == 0:
            return ''

        elif num < 20:
            return self.words1to19[num] + ' '

        elif num < 100:
            return self.words10to90[num // 10] + ' ' + self.convert(num % 10)

        else:
            return self.words1to19[num // 100] + ' Hundred ' + self.convert(num % 100)

        