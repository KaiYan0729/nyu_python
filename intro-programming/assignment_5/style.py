#!/usr/bin/env python3
#example_1
if __name__ == '__main__':
    main()
	
foo = long_function_name(var_one, var_two,
    var_three, var_four)


def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)

#example_2
# operators: prefix or postfix?
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

#example_3
def top_level_func():
    print("important processing going on here")

def second_func():


    print("another gravely important function")


#example_4
def topLevelFunc():
    print("important processing going on here")
    mixedCaseVariables = True