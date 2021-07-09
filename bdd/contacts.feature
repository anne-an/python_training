Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <middlename> and <lastname>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | firstname  | middlename  | lastname  |
  | firstname1 | middlename1 | lastname1 |
  | firstname2 | middlename2 | lastname2 |


Scenario: Delete contact
  Given a non-empty contact list
  Given a contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact


Scenario Outline: Modify contact
  Given a non-empty contact list
  Given a contact from the list
  Given a contact with <firstname>, <middlename> and <lastname>
  When I modify contact information
  Then the new contact list is equal to the old one with the modified contact

    Examples:
  | firstname  | middlename  | lastname  |
  | firsttest1 | middletest1 | lasttest1 |
  | firsttest2 | middletest2 | lasttest2 |