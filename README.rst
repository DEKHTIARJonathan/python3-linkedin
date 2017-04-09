Python3-LinkedIn
================

|LinkedIn| |Build Status|

Python interface to the LinkedIn API

This library provides a pure Python interface to the LinkedIn
**Profile**, **Group**, **Company**, **Jobs**, **Search**, **Share**,
**Network** and **Invitation** REST APIs.

`LinkedIn <https://developer.linkedin.com>`__ provides a service that
lets people bring their LinkedIn profiles and networks with them to your
site or application via their OAuth based API. This library provides a
lightweight interface over a complicated LinkedIn OAuth based API to
make it for python programmers easy to use.

Acknowledgement
---------------

-  This library was created by `Ozgur
   Vatansever <https://github.com/ozgur>`__.
-  In 2016, the library was converted to Python 3 by `Marshall
   Lusher <https://github.com/marshalllusher>`__

Maintainer : `Jonathan Dekhtiar <https://github.com/DEKHTIARJonathan>`__

Contributors: \* `Ozgur Vatansever <https://github.com/ozgur>`__ \*
`Marshall Lusher <https://github.com/marshalllusher>`__ \* `Jonathan
Dekhtiar <https://github.com/DEKHTIARJonathan>`__ \* `Abraham
Williams <https://github.com/abraham>`__ \* `Matthew A.
Russell <https://github.com/ptwobrussell>`__ \* `Samuel
Marks <https://github.com/SamuelMarks>`__ \* `Emlyn
Clay <https://github.com/EmlynC>`__ \* `Ivan
Kravets <https://github.com/ivankravets>`__ \* `Devin
Barry <https://github.com/devinbarry>`__ \* `Josh
Owen <https://github.com/joshowen>`__ \* `Chengxin
Cai <https://github.com/iacxc>`__ \* `Yuri
Prezument <https://github.com/yprez>`__ \* `Jay
Zeng <https://github.com/jayzeng>`__ \* `Julien
Muniak <https://github.com/Darune>`__ \* `John
Franey <https://github.com/johnfraney>`__ \* `Adrian
Sgn <https://github.com/adrian-sgn>`__ \* `Luca Adalberto
Vandro <https://github.com/lucavandro>`__ \*
`Jack <https://github.com/mclate>`__ \* `Scotty
Delta <https://github.com/scottydelta>`__ \* `Michael
Blakeley <https://github.com/mblakele>`__ \* `Song
Zhen-Gang <https://github.com/lyroge>`__ \* `Ismail
Coskuner <https://github.com/ismix>`__ \*
`Marshyang <https://github.com/marshyang>`__ \* `Iurii
Kudriavtsev <https://github.com/ikudriavtsev>`__ \* `Kartik
Ayyar <https://github.com/ayyar>`__ \* `Kit
Sunde <https://github.com/kitsunde>`__ \* `Patrick
Müssig <https://github.com/b3nelof0n>`__

Installation
------------

Available with the Python Package Index:
https://pypi.python.org/pypi/python3-linkedin

.. code:: shell

    pip install python3-linkedin

If prefered, the library can be compiled with following commands:

.. code:: shell

    ## First clone the repository
    git clone https://github.com/DEKHTIARJonathan/python3-linkedin.git

    ## Then install the library
    python setup.py install

Authentication
--------------

The LinkedIn REST API now supports the **OAuth 2.0** protocol for
authentication. This package provides a full OAuth 2.0 implementation
for connecting to LinkedIn as well as an option for using an OAuth 1.0a
flow that can be helpful for development purposes or just accessing your
own data.

HTTP API example
~~~~~~~~~~~~~~~~

Please declare and setup a new application on the `LinkedIn Developer
Console <https://www.linkedin.com/developer/apps>`__

Set ``LINKEDIN_API_KEY`` and ``LINKEDIN_API_SECRET``, configure your app
to redirect to ``http://localhost:8080/code``, then execute:

0. ``http_api.py``
1. Visit ``http://localhost:8080`` in your browser, curl or similar
2. A tab in your browser will open up, give LinkedIn permission there
3. You'll then be presented with a list of available routes, hit any,
   e.g.:
4. ``curl -XGET http://localhost:8080/get_profile``

Developer Authentication
~~~~~~~~~~~~~~~~~~~~~~~~

To connect to LinkedIn as a developer or just to access your own data,
you don't even have to implement an OAuth 2.0 flow that involves
redirects. You can simply use the 4 credentials that are provided to you
in your LinkedIn appliation as part of an OAuth 1.0a flow and
immediately access your data. Here's how:

.. code:: python

    from linkedin import linkedin

    # Define CONSUMER_KEY, CONSUMER_SECRET,  
    # USER_TOKEN, and USER_SECRET from the credentials
    # provided in your LinkedIn application

    # Instantiate the developer authentication class

    authentication = linkedin.LinkedInDeveloperAuthentication(
                        CONSUMER_KEY,
                        CONSUMER_SECRET,
                        USER_TOKEN,
                        USER_SECRET,
                        RETURN_URL,
                        linkedin.PERMISSIONS.enums.values()
                    )

    # Optionally one can send custom "state" value that will be returned from OAuth server
    # It can be used to track your user state or something else (it's up to you)
    # Be aware that this value is sent to OAuth server AS IS - make sure to encode or hash it

    # authorization.state = 'your_encoded_message'

    # Pass it in to the app...

    application = linkedin.LinkedInApplication(authentication)

    # Use the app....

    application.get_profile()

Production Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~

In order to use the LinkedIn OAuth 2.0, you need to have these two keys
from the from the `LinkedIn Developer
Console <https://www.linkedin.com/developer/apps>`__:

.. code:: python

    APPLICATON_KEY    = '##############'
    APPLICATON_SECRET = '################'

You can get more detail about the Oauth2 authentication process from
`here <https://developer.linkedin.com/docs/oauth2>`__.

LinkedIn redirects the user back to your website's URL after granting
access (giving proper permissions) to your application. We call that url
**RETURN URL**. Assuming your return url is **https://localhost:8000**,
you can write something like this:

.. code:: python

    from linkedin import linkedin

    APPLICATON_KEY    = '##############'
    APPLICATON_SECRET = '################'

    RETURN_URL = 'http://localhost:8000'

    authentication = linkedin.LinkedInAuthentication(
                        APPLICATON_KEY,
                        APPLICATON_SECRET,
                        RETURN_URL,
                        linkedin.PERMISSIONS.enums.values()
                    )

    # Optionally one can send custom "state" value that will be returned from OAuth server
    # It can be used to track your user state or something else (it's up to you)
    # Be aware that this value is sent to OAuth server AS IS - make sure to encode or hash it
    #authorization.state = 'your_encoded_message'

    print (authentication.authorization_url)  # open this url on your browser

When you grant access to the application, you will be redirected to the
return url with the following query strings appended to your
**RETURN\_URL**:

.. code:: python

    "http://localhost:8000/?code=#############################################&state=########################"

This url contains the value of the **authorization\_code**. After
setting it by hand, we can call the **.get\_access\_token()** to get the
actual token.

.. code:: python

    from linkedin import linkedin

    APPLICATON_KEY    = '##############'
    APPLICATON_SECRET = '################'

    RETURN_URL = 'http://localhost:8000'

    authentication = linkedin.LinkedInAuthentication(
                        APPLICATON_KEY,
                        APPLICATON_SECRET,
                        RETURN_URL,
                        linkedin.PERMISSIONS.enums.values()
                    )

    authentication.authorization_code = '#############################################'
    result = authentication.get_access_token()

    print ("Access Token:", result.access_token)
    print ("Expires in (seconds):", result.expires_in)

After you get the access token, you are now permitted to make API calls
on behalf of the user who granted access to you app. In addition to
that, in order to prevent from going through the OAuth flow for every
consecutive request, one can directly assign the access token obtained
before to the application instance.

.. code:: python

    from linkedin import linkedin

    application = linkedin.LinkedInApplication(token='###################################')

Quick Usage From Python Interpreter
-----------------------------------

For testing the library using an interpreter, you can benefit from the
test server.

.. code:: python

    from linkedin import server
    application = server.quick_api(KEY, SECRET)

This will print the authorization url to the screen. Go into that URL
using a browser to grant access to the application. After you do so, the
method will return with an API object you can now use.

Profile API
-----------

The Profile API returns a member's LinkedIn profile. You can use this
call to return one of two versions of a user's profile which are
**public profile** and **standard profile**. For more information, check
out the
`documentation <https://developers.linkedin.com/documents/profile-api>`__.

.. code:: python

    application.get_profile()
    {u'firstName': u'ozgur',
     u'headline': u'This is my headline',
     u'lastName': u'vatansever',
     u'siteStandardProfileRequest': {u'url': u'https://www.linkedin.com/profile/view?id=46113651&authType=name&authToken=Egbj&trk=api*a101945*s101945*'}}

There are many **field selectors** that enable the client fetch more
information from the API. All of them used by each API are listed
`here <https://developers.linkedin.com/documents/field-selectors>`__.

.. code:: python

    application.get_profile(selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations'])
    {u'distance': 0,
     u'educations': {u'_total': 1,
      u'values': [{u'activities': u'This is my activity and society field',
        u'degree': u'graduate',
        u'endDate': {u'year': 2009},
        u'fieldOfStudy': u'computer science',
        u'id': 42611838,
        u'notes': u'This is my additional notes field',
        u'schoolName': u'\u0130stanbul Bilgi \xdcniversitesi',
        u'startDate': {u'year': 2004}}]},
     u'firstName': u'ozgur',
     u'id': u'COjFALsKDP',
     u'lastName': u'vatansever',
     u'location': {u'country': {u'code': u'tr'}, u'name': u'Istanbul, Turkey'},
     u'numConnections': 13}

Connections API
---------------

The Connections API returns a list of **1st degree** connections for a
user who has granted access to their account. For more information, you
check out its
`documentation <https://developers.linkedin.com/documents/connections-api>`__.

To fetch your connections, you simply call **.get\_connections()**
method with proper GET querystring:

.. code:: python

    application.get_connections()
    {u'_total': 13,
     u'values': [{u'apiStandardProfileRequest': {u'headers': {u'_total': 1,
         u'values': [{u'name': u'x-li-auth-token', u'value': u'name:16V1033'}]},
        u'url': u'https://api.linkedin.com/v1/people/lddvGtD5xk'},
       u'firstName': u'John',
       u'headline': u'Ruby',
       u'id': u'2323SDFSsfd34',
       u'industry': u'Computer Software',
       u'lastName': u'DOE',
       u'location': {u'country': {u'code': u'tr'}, u'name': u'Istanbul, Turkey'},
       u'siteStandardProfileRequest': {u'url': u'https://www.linkedin.com/profile/view?id=049430532&authType=name&authToken=16V8&trk=api*a101945*s101945*'}},
       ....

    application.get_connections(selectors=['headline', 'first-name', 'last-name'], params={'start':10, 'count':5})

Search API
----------

There are 3 types of Search APIs. One is the **People Search** API,
second one is the **Company Search** API and the last one is **Jobs
Search** API.

The People Search API returns information about people. It lets you
implement most of what shows up when you do a search for "People" in the
top right box on LinkedIn.com. You can get more information from
`here <https://developers.linkedin.com/documents/people-search-api>`__.

.. code:: python

    application.search_profile(selectors=[{'people': ['first-name', 'last-name']}], params={'keywords': 'apple microsoft'})
    # Search URL is https://api.linkedin.com/v1/people-search:(people:(first-name,last-name))?keywords=apple%20microsoft

    {u'people': {u'_count': 10,
      u'_start': 0,
      u'_total': 2,
      u'values': [
       {u'firstName': u'John', u'lastName': 'Doe'},
       {u'firstName': u'Jane', u'lastName': u'Doe'}
      ]}}

The Company Search API enables search across company pages. You can get
more information from
`here <https://developers.linkedin.com/documents/company-search>`__.

.. code:: python

    application.search_company(selectors=[{'companies': ['name', 'universal-name', 'website-url']}], params={'keywords': 'apple microsoft'})
    # Search URL is https://api.linkedin.com/v1/company-search:(companies:(name,universal-name,website-url))?keywords=apple%20microsoft

    {u'companies': {u'_count': 10,
      u'_start': 0,
      u'_total': 1064,
      u'values': [{u'name': u'Netflix',
        u'universalName': u'netflix',
        u'websiteUrl': u'httsp://netflix.com'},
       {u'name': u'Alliance Data',
        u'universalName': u'alliance-data',
        u'websiteUrl': u'www.alliancedata.com'},
       {u'name': u'GHA Technologies',
        u'universalName': u'gha-technologies',
        u'websiteUrl': u'www.gha-associates.com'},
       {u'name': u'Intelligent Decisions',
        u'universalName': u'intelligent-decisions',
        u'websiteUrl': u'https://www.intelligent.net'},
       {u'name': u'Mindfire Solutions',
        u'universalName': u'mindfire-solutions',
        u'websiteUrl': u'www.mindfiresolutions.com'},
       {u'name': u'Babel Media',
        u'universalName': u'babel-media',
        u'websiteUrl': u'https://www.babelmedia.com/'},
       {u'name': u'Milestone Technologies',
        u'universalName': u'milestone-technologies',
        u'websiteUrl': u'www.milestonepowered.com'},
       {u'name': u'Denali Advanced Integration',
        u'universalName': u'denali-advanced-integration',
        u'websiteUrl': u'www.denaliai.com'},
       {u'name': u'MicroAge',
        u'universalName': u'microage',
        u'websiteUrl': u'www.microage.com'},
       {u'name': u'TRUSTe',
        u'universalName': u'truste',
        u'websiteUrl': u'https://www.truste.com/'}]}}

The Job Search API enables search across LinkedIn's job postings. You
can get more information from
`here <https://developers.linkedin.com/documents/job-search-api>`__.

.. code:: python

    application.search_job(selectors=[{'jobs': ['id', 'customer-job-code', 'posting-date']}], params={'title': 'python', 'count': 2})
    {u'jobs': {u'_count': 2,
      u'_start': 0,
      u'_total': 206747,
      u'values': [{u'customerJobCode': u'0006YT23WQ',
        u'id': 5174636,
        u'postingDate': {u'day': 21, u'month': 3, u'year': 2013}},
       {u'customerJobCode': u'00023CCVC2',
        u'id': 5174634,
        u'postingDate': {u'day': 21, u'month': 3, u'year': 2013}}]}}

Group API
---------

The Groups API provides rich access to read and interact with LinkedIn’s
groups functionality. You can get more information from
`here <https://developers.linkedin.com/documents/groups-api>`__. By the
help of the interface, you can fetch group details, get your group
memberships as well as your posts for a specific group which you are a
member of.

.. code:: python

    application.get_group(41001)
    {u'id': u'41001', u'name': u'Object Oriented Programming'}

    application.get_memberships(params={'count': 20})
    {u'_total': 1,
     u'values': [{u'_key': u'25827',
       u'group': {u'id': u'25827', u'name': u'Python Community'},
       u'membershipState': {u'code': u'member'}}]}

    application.get_posts(41001)

    application.get_post_comments(
        %POST_ID%,
        selectors=[
            {"creator": ["first-name", "last-name"]},
            "creation-timestamp",
            "text"
        ],
        params={"start": 0, "count": 20}
    )

You can also submit a new post into a specific group.

.. code:: python

    title = 'Scala for the Impatient'
    summary = 'A new book has been published'
    submitted_url = 'https://horstmann.com/scala/'
    submitted_image_url = 'https://horstmann.com/scala/images/cover.png'
    description = 'It is a great book for the keen beginners. Check it out!'

    application.submit_group_post(41001, title, summary, submitted_url, submitted_image_url, description)

Company API
-----------

The Company API: \* Retrieves and displays one or more company profiles
based on the company ID or universal name. \* Returns basic company
profile data, such as name, website, and industry. \* Returns handles to
additional company content, such as RSS stream and Twitter feed.

You can query a company with either its **ID** or **Universal Name**.
For more information, you can check out the documentation
`here <https://developers.linkedin.com/documents/company-lookup-api-and-fields>`__.

.. code:: python

    application.get_companies(company_ids=[1035], universal_names=['apple'], selectors=['name'], params={'is-company-admin': 'true'})
    # 1035 is Microsoft
    # The URL is as follows: https://api.linkedin.com/v1/companies::(1035,universal-name=apple)?is-company-admin=true

    {u'_total': 2,
     u'values': [{u'_key': u'1035', u'name': u'Microsoft'},
      {u'_key': u'universal-name=apple', u'name': u'Apple'}]}

    # Get the latest updates about Microsoft
    application.get_company_updates(1035, params={'count': 2})
    {u'_count': 2,
     u'_start': 0,
     u'_total': 58,
     u'values': [{u'isCommentable': True,
       u'isLikable': True,
       u'isLiked': False,
       u'numLikes': 0,
       u'timestamp': 1363855486620,
       u'updateComments': {u'_total': 0},
       u'updateContent': {u'company': {u'id': 1035, u'name': u'Microsoft'},
        u'companyJobUpdate': {u'action': {u'code': u'created'},
         u'job': {u'company': {u'id': 1035, u'name': u'Microsoft'},
          u'description': u'Job Category: SalesLocation: Sacramento, CA, USJob ID: 812346-106756Division: Retail StoresStore...',
          u'id': 5173319,
          u'locationDescription': u'Sacramento, CA, US',
          u'position': {u'title': u'Store Manager, Specialty Store'},
          u'siteJobRequest': {u'url': u'https://www.linkedin.com/jobs?viewJob=&jobId=5173319'}}}},
       u'updateKey': u'UNIU-c1035-5720424522989961216-FOLLOW_CMPY',
       u'updateType': u'CMPY'},
      {u'isCommentable': True,
       u'isLikable': True,
       u'isLiked': False,
       u'numLikes': 0,
       u'timestamp': 1363855486617,
       u'updateComments': {u'_total': 0},
       u'updateContent': {u'company': {u'id': 1035, u'name': u'Microsoft'},
        u'companyJobUpdate': {u'action': {u'code': u'created'},
         u'job': {u'company': {u'id': 1035, u'name': u'Microsoft'},
          u'description': u'Job Category: Software Engineering: TestLocation: Redmond, WA, USJob ID: 794953-81760Division:...',
          u'id': 5173313,
          u'locationDescription': u'Redmond, WA, US',
          u'position': {u'title': u'Software Development Engineer in Test, Senior-IEB-MSCIS (794953)'},
          u'siteJobRequest': {u'url': u'https://www.linkedin.com/jobs?viewJob=&jobId=5173313'}}}},
       u'updateKey': u'UNIU-c1035-5720424522977378304-FOLLOW_CMPY',
       u'updateType': u'CMPY'}]}

You can follow or unfollow a specific company as well.

.. code:: python

    application.follow_company(1035)
    True

    application.unfollow_company(1035)
    True

Job API
-------

The Jobs APIs provide access to view jobs and job data. You can get more
information from its
`documentation <https://developers.linkedin.com/documents/job-lookup-api-and-fields>`__.

.. code:: python

    application.get_job(job_id=5174636)
    {u'active': True,
     u'company': {u'id': 2329, u'name': u'Schneider Electric'},
     u'descriptionSnippet': u"The Industrial Accounts Sales Manager is a quota carrying senior sales position principally responsible for generating new sales and growing company's share of wallet within the industrial business, contracting business and consulting engineering business. The primary objective is to build and establish strong and lasting relationships with technical teams and at executive level within specific in",
     u'id': 5174636,
     u'position': {u'title': u'Industrial Accounts Sales Manager'},
     u'postingTimestamp': 1363860033000}

You can also fetch you job bookmarks.

.. code:: python

    application.get_job_bookmarks()
    {u'_total': 0}

Share API
---------

Network updates serve as one of the core experiences on LinkedIn, giving
users the ability to share rich content to their professional network.
You can get more information from
`here <https://developers.linkedin.com/documents/share-api>`__.

::

    application.submit_share('Posting from the API using JSON', 'A title for your share', None, 'https://www.linkedin.com', 'https://d.pr/3OWS')
    {'updateKey': u'UNIU-8219502-5705061301949063168-SHARE'
     'updateURL': 'https://www.linkedin.com/updates?discuss=&amp;scope=8219502&amp;stype=M&amp;topic=5705061301949063168&amp;type=U&amp;a=aovi'}

Network API
-----------

The Get Network Updates API returns the users network updates, which is
the LinkedIn term for the user's feed. This call returns most of what
shows up in the middle column of the LinkedIn.com home page, either for
the member or the member's connections. You can get more information
from
`here <https://developers.linkedin.com/documents/get-network-updates-and-statistics-api>`__.

There are many network update types. You can look at them by importing
**NETWORK\_UPDATES** enumeration.

.. code:: python

    from linkedin.linkedin import NETWORK_UPDATES
    print NETWORK_UPDATES.enums
    {'APPLICATION': 'APPS',
     'CHANGED_PROFILE': 'PRFU',
     'COMPANY': 'CMPY',
     'CONNECTION': 'CONN',
     'EXTENDED_PROFILE': 'PRFX',
     'GROUP': 'JGRP',
     'JOB': 'JOBS',
     'PICTURE': 'PICT',
     'SHARED': 'SHAR',
     'VIRAL': 'VIRL'}

    update_types = (NETWORK_UPDATES.CONNECTION, NETWORK_UPDATES.PICTURE)
    application.get_network_updates(update_types)

    {u'_total': 1,
     u'values': [{u'isCommentable': True,
       u'isLikable': True,
       u'isLiked': False,
       u'numLikes': 0,
       u'timestamp': 1363470126509,
       u'updateComments': {u'_total': 0},
       u'updateContent': {u'person': {u'apiStandardProfileRequest': {u'headers': {u'_total': 1,
           u'values': [{u'name': u'x-li-auth-token', u'value': u'name:Egbj'}]},
          u'url': u'https://api.linkedin.com/v1/people/COjFALsKDP'},
         u'firstName': u'ozgur',
         u'headline': u'This is my headline',
         u'id': u'COjFALsKDP',
         u'lastName': u'vatansever',
         u'siteStandardProfileRequest': {u'url': u'https://www.linkedin.com/profile/view?id=46113651&authType=name&authToken=Egbj&trk=api*a101945*s101945*'}}},
       u'updateKey': u'UNIU-46113651-5718808205493026816-SHARE',
       u'updateType': u'SHAR'}]}

Invitation API
--------------

The Invitation API allows your users to invite people they find in your
application to their LinkedIn network. You can get more information from
`here <https://developers.linkedin.com/documents/invitation-api>`__.

.. code:: python

    from linkedin.models import LinkedInRecipient, LinkedInInvitation
    recipient = LinkedInRecipient(None, 'john.doe@python.org', 'John', 'Doe')
    print recipient.json
    {'person': {'_path': '/people/email=john.doe@python.org',
      'first-name': 'John',
      'last-name': 'Doe'}}

    invitation = LinkedInInvitation('Hello John', "What's up? Can I add you as a friend?", (recipient,), 'friend')
    print invitation.json
    {'body': "What's up? Can I add you as a friend?",
     'item-content': {'invitation-request': {'connect-type': 'friend'}},
     'recipients': {'values': [{'person': {'_path': '/people/email=john.doe@python.org',
         'first-name': 'John',
         'last-name': 'Doe'}}]},
     'subject': 'Hello John'}

    application.send_invitation(invitation)
    True

Throttle Limits
---------------

LinkedIn API keys are throttled by default. You should take a look at
the `Throttle Limits
Documentation <https://developer.linkedin.com/documents/throttle-limits>`__
to get more information about it.

.. |LinkedIn| image:: https://img4.hostingpics.net/pics/514667Capture.png
   :target: http://developer.linkedin.com
.. |Build Status| image:: https://travis-ci.org/DEKHTIARJonathan/python3-linkedin.svg?branch=master
   :target: https://travis-ci.org/DEKHTIARJonathan/python3-linkedin
