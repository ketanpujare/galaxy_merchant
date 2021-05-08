from conversion import roman_calculation, ROMAN_NUMS

class Galaxy_Merchant:
    def __init__(self):
        """
        Main Class for Galaxy Merchant
        """

        self.galaxy_currency = dict()
        self.metal_values = dict()
    
    def process_currency(self, currency_list):
        """
        Stores Mapping of Global Currency to Roman
        """
        for currency in currency_list:
            self.galaxy_currency[currency[0]] = currency[-1]

    def currency_mapping(self, currency_list):
        """
        Coverts global currency to Roman currency eg. glob glob to "II"
        """
        return ''.join([self.galaxy_currency.get(cur) for cur in currency_list])

    def get_numeric_value(self, currency_list):
        """
        Returns Decimal value of global currency
        """
        return roman_calculation(self.currency_mapping(currency_list))

    def get_metal_values(self, metal_data):
        """
        Calculate & Stores Metal Values
        """
        self.metal_values[metal_data[-4]] = float(float(metal_data[-2])/self.get_numeric_value(metal_data[:-4]))

    def process_metal_values(self, metal_list):
        for metal in metal_list:
            self.get_metal_values(metal)

    def process_questions(self, question_data):
        for question in question_data:
            try:
                if 'Credits' in question:
                    price = self.metal_values[question[-2]] * self.get_numeric_value(question[4:-2])
                    print('{} is {} Credits.'.format(' '.join(question[4:-1]),price))
                else:
                    price = self.get_numeric_value(question[3:-1])
                    print('{} is {} Credits.'.format(' '.join(question[3:-1]),price))
            except:
                print('I have no idea what you are talking about.')

    def process_inputs(self, currency_list, metal_input, question_input, other):
        self.process_currency(currency_list)
        self.process_metal_values(metal_input)
        self.process_questions(question_input)


    def input_parser(self,input):
        galaxy_currency = list()
        metal_values = list()
        questions = list()
        other = list()

        inputs = input.strip().split('\n')
        
        for single_input in inputs:
            input_div = single_input.strip().split(' ')
            if input_div[-1] in ROMAN_NUMS.keys():
                galaxy_currency.append(input_div)
            elif 'Credits' == input_div[-1]:
                metal_values.append(input_div)
            elif '?' == input_div[-1]:
                questions.append(input_div)
            else:
                other.append(input_div)
        return galaxy_currency, metal_values, questions, other


input = """glob is I
prok is V
pish is X
tegj is L
glob glob Silver is 34 Credits
glob prok Gold is 57800 Credits
pish pish Iron is 3910 Credits
how much is pish tegj glob glob ?
how many Credits is glob prok Silver ?
how many Credits is glob prok Gold ?
how many Credits is glob prok Iron ?
how much wood could a woodchuck chuck if a woodchuck could chuck wood ?"""

if __name__ == '__main__':
    obj = Galaxy_Merchant()
    parser_out = obj.input_parser(input)
    obj.process_inputs(*parser_out)