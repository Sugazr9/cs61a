test = {
  'name': 'factorial_ok',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'The return statement in the recursive case is missing',
          'choices': [
            'The return statement in the recursive case is missing',
            'The base case is flawed: it should be n <= 0',
            'This function is different from the one above',
            'The variable n does not change, causing a infinite loop'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          Consider this implementation of the factorial function:
          def factorial(n):
              if n == 0:
                  return 1
              else:
                  n * factorial(n-1)
          
          What is wrong with it?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
