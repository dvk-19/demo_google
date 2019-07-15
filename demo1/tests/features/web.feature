@web @google

Feature: Google Search Engine
 As I browse the web
 I can find required information

Scenario: Test Something

Scenario: Basic Google Search
 Given The Google Search Page is displayed
 When The user searches for Firefox
 Then the results are shown for Firefox

Scenario: Select the link to download
 Given The results are displayed
 When We click the first link
 Then The firefox page is displayed

