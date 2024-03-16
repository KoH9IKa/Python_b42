

Scenario Outline: Add new group
  Given group list
  Given group with {name} {header} {footer}
  When add new group
  Then new groups list is equal to old groups list with added group


  Examples:
  |name|header|footer|
  |name1|header1|footer1|
  |name2|header2|footer2|