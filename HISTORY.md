# Version History

## 0.5.3_preview / 2022-01-12

- Remove support for shared types

## 0.5.1_preview / 2021-12-18

- Remove reliance on Asset v1-preview routes

## 0.5.0_preview / 2021-12-06

- Added support for reading shared streams

## 0.4.10_preview / 2021-12-01

- Set default value of ValueClass to None for Streams.getWindowValues(Url) and reordered this argument to after all required arguments
- Add query parameter to StreamViews.getStreamViews

## 0.4.9_preview / 2021-11-30

- Update pipelines to reference internal analysis templates

## 0.4.8_preview / 2021-11-20

- Delete sample_local_testing_program and add appsettings.json to gitignore

## 0.4.7_preview / 2021-11-20

- Delete requests session when the BaseClient is disposed of

## 0.4.6_preview / 2021-11-11

- Modified BaseClient to use a single requests session
- Added URL encoding to Securable and Patchable Securable classes

## 0.4.5_preview / 2021-10-21

- Enhanced data view data form parameter support to allow for form=default
- Updated data view function documentation
- Updated sample test script to match data view sample syntax

## 0.4.4_preview / 2021-10-14

- Update base client references in DataViews class

## 0.4.3_preview / 2021-09-31

- Add support for special characters in Ids by url encoding them

## 0.4.2_preview / 2021-09-30

- Resolve issue with data view data calls accepting urls as input parameters

## 0.4.1_preview / 2021-09-10

- Added StreamViews to EDS Client

## 0.4.0_preview / 2021-08-26

- Added support for managing ACLs on securable collections
- Support for additional collections (Users, Topics, Subscriptions, etc.)
- Split related collections out of the Assts and Streams classes

## 0.3.6_preview / 2021-08-09

- Added stored value retrieval for data views
- Updated dependencies
- Cleaned up gitignore

## 0.3.5_preview / 2021-07-29

- Added index collection value retrieval to the Streams class

## 0.3.4_preview / 2021-07-28

- Added filter expressions for the Streams class's getRangeValues and getRangeValuesInterpolated functions

## 0.3.3_preview / 2021-07-28

- Interpolation/Extrapolation mode enum handling

## 0.3.2_preview / 2021-07-15

- Updated dependencies

## 0.3.1_preview / 2021-07-12

- Added new StatusConfiguration and StatusDefinitionType classes to sync with latest assets REST API

## 0.3.0_preview / 2021-07-09

- Added required features for sample community steps

## 0.2.7_preview / 2021-06-01

- Updated asset status APIs to read enum string instead of int

## 0.2.6_preview / 2021-05-24

- Added summaries to DataView Field class definition

## 0.2.5_preview / 2021-05-19

- Add support for paging in getWindowValues
- Switch to using preview route in Assets client

## 0.2.4_preview / 2021-05-18

- Changed function names from createAsset[Type] to getOrCreateAsset[Type]
- Switch from v1-preview to v1 route in DataViews client

## 0.2.3_preview / 2021-05-07

- Fix typo in DataView.py

## 0.2.2_preview / 2021-05-05

- Add comprehensive handling for optional enumeration properties

## 0.2.1_preview / 2021-05-03

- Add check for null SdsTypeProperty InterpolationMode

## 0.2.0_preview / 2021-04-23

- Major refactor of classes and parameters, including many breaking changes
- Added OCS Assets models and API endpoints
- Added type hints for all API models and endpoints

## 0.1.18_preview / 2021-03-24

- Updated pipeline to use internal agent pool
- Updated pipeline to reference main branch

## 0.1.17_preview / 2021-02-24

- Updated ocsclients and edsclients to expose the baseclient

## 0.1.16_preview / 2021-01-26

- Updated versions and readme. 0.1.15 skipped due to pipeline issues

## 0.1.14_preview / 2021-01-25

- Updated dependencies

## 0.1.13_preview / 2020-10-20

- Added patchMetadata method to edit stream metadata

## 0.1.12_preview / 2020-07-24

- Fix issue in published dependency on requests 2.23.0

## 0.1.11_preview / 2020-07-23

- Fix implementation of `reversed` flag for stream API calls
- General code cleanup & formatting
- Remove unnecessary pylint disable rules
- Added EDSClient to support API calls against SDS in Edge Data Store

## 0.1.10_preview / 2020-07-16

- Updated first/next page URL links

## 0.1.9_preview / 2020-06-11

- Updated dependencies

## 0.1.8_preview / 2020-05-06

- Added weekly schedule to analysis pipeline

## 0.1.7_preview / 2020-05-05

- Updated to use Polaris in place of Coverity

## 0.1.6_preview / 2020-05-04

- Added overload of OCSClient that allows PKCE authentication

## 0.1.5.2_internal / 2020-04-02

- Updated sample to use `BaseClient` `request` method

## 0.1.5.1_internal / 2020-03-31

- Minor code cleanup

## 0.1.5_preview / 2020-03-24

- Updated to latest Data Views Preview API

## 0.1.4_preview / 2020-03-06

- Bug fixes for paging

## 0.1.3_preview / 2020-02-19

- Bug fixes to fieldset and asserts

## 0.1.2_preview / 2020-02-19

- Fixed folder casing

## 0.1.1_preview / 2020-02-19

- Fixed folder casing

## 0.1.0_preview / 2020-02-19

- Updated to latest Data Views Preview API

## 0.0.36.4_internal / 2020-02-18

- Added 3rd party license file

## 0.0.36.3_internal / 2020-01-30

- Added complete dependencies list

## 0.0.36.2_internal / 2019-12-19

- Removed duplicate statement

## 0.0.36.1_internal / 2019-12-13

- Updated build pipeline

## 0.0.36_preview / 2019-12-11

- Updated build pipeline

## 0.0.35.3_internal / 2019-12-04

- Migrate build pipeline

## 0.0.35.2_internal / 2019-12-03

- Set up library build pipeline

## 0.0.35.1_internal / 2019-11-12

- Updated README documentation

## 0.0.35_preview / 2019-09-04

- Updated fromDictionary to handle None

## 0.0.34_preview / 2019-09-03

- Updates to SDS and DataViews API

## 0.0.33_preview / 2019-09-03

- Updates to SDS and DataViews API

## 0.0.32_preview / 2019-08-22

- Updated repository URL

## 0.0.31_preview / 2019-08-15

- Initial move, begin version tracking
