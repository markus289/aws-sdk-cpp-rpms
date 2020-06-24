Name:           aws-sdk-cpp
Version:        1.7.361
Release:        1%{?dist}
Summary:        Amazon Web Services SDK for C++
License:        ASL 2.0
URL:            https://github.com/aws/%{name}
Source0:        https://github.com/aws/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%if 0%{?el7}
BuildRequires:  cmake3 >= 3.1
%else
BuildRequires:  cmake >= 3.1
%endif

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  aws-c-common-devel
BuildRequires:  aws-c-event-stream-devel
BuildRequires:  aws-checksums-devel
BuildRequires:  libcurl-devel
BuildRequires:  openssl-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  zlib-devel

Requires:       aws-c-common
Requires:       aws-c-event-stream
Requires:       aws-checksums
Requires:       libcurl
Requires:       openssl-libs
Requires:       pulseaudio-libs
Requires:       zlib

%description
The Amazon Web Services (AWS) SDK for C++ provides a modern C++ interface for
AWS. It is meant to be performant and fully functioning with low- and
high-level SDKs, while minimizing dependencies and providing platform
portability (Windows, OSX, Linux, and mobile).

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       aws-c-common-devel
Requires:       aws-c-event-stream-devel
Requires:       aws-checksums-devel
Requires:       libcurl-devel
Requires:       openssl-devel
Requires:       zlib-devel

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-sdk-cpp.

%prep
%autosetup
sed -i -e 's/ "-Werror" "-pedantic"//' cmake/compiler_settings.cmake

%build
%if 0%{?el7}
%cmake3 \
    -DBUILD_SHARED_LIBS:BOOL=TRUE \
    -DBUILD_DEPS:BOOL=FALSE \
    -DAUTORUN_UNIT_TESTS:BOOL=FALSE \
    -DCUSTOM_MEMORY_MANAGEMENT:BOOL=FALSE \
    -DBUILD_ONLY='accessanalyzer;access-management;acm;acm-pca;alexaforbusiness;amplify;apigateway;apigatewaymanagementapi;apigatewayv2;appconfig;application-autoscaling;application-insights;appmesh;appstream;appsync;athena;autoscaling;autoscaling-plans;AWSMigrationHub;awstransfer;backup;batch;budgets;ce;chime;cloud9;clouddirectory;cloudformation;cloudfront;cloudhsm;cloudhsmv2;cloudsearch;cloudsearchdomain;cloudtrail;codeartifact;codebuild;codecommit;codedeploy;codeguruprofiler;codeguru-reviewer;codepipeline;codestar;codestar-connections;codestar-notifications;cognito-identity;cognito-idp;cognito-sync;comprehend;comprehendmedical;compute-optimizer;config;connect;connectparticipant;cur;dataexchange;datapipeline;datasync;dax;detective;devicefarm;directconnect;discovery;dlm;dms;docdb;ds;dynamodb;dynamodbstreams;ebs;ec2;ec2-instance-connect;ecr;ecs;eks;elasticache;elasticbeanstalk;elasticfilesystem;elastic-inference;elasticloadbalancing;elasticloadbalancingv2;elasticmapreduce;elastictranscoder;email;es;eventbridge;events;firehose;fms;forecast;forecastquery;frauddetector;gamelift;glacier;globalaccelerator;glue;greengrass;groundstation;guardduty;health;iam;identity-management;imagebuilder;importexport;inspector;iot;iot1click-devices;iot1click-projects;iotanalytics;iot-data;iotevents;iotevents-data;iot-jobs-data;iotsecuretunneling;iotsitewise;iotthingsgraph;kafka;kendra;kinesis;kinesisanalytics;kinesisanalyticsv2;kinesisvideo;kinesis-video-archived-media;kinesis-video-media;kinesis-video-signaling;kms;lakeformation;lambda;lex;lex-models;license-manager;lightsail;logs;machinelearning;macie;macie2;managedblockchain;marketplace-catalog;marketplacecommerceanalytics;marketplace-entitlement;mediaconnect;mediaconvert;medialive;mediapackage;mediapackage-vod;mediastore;mediastore-data;mediatailor;meteringmarketplace;migrationhub-config;mobile;mobileanalytics;monitoring;mq;mturk-requester;neptune;networkmanager;opsworks;opsworkscm;organizations;outposts;personalize;personalize-events;personalize-runtime;pi;pinpoint;pinpoint-email;polly;polly-sample;pricing;qldb;qldb-session;queues;quicksight;ram;rds;rds-data;redshift;rekognition;resource-groups;resourcegroupstaggingapi;robomaker;route53;route53domains;route53resolver;s3;s3control;s3-encryption;sagemaker;sagemaker-a2i-runtime;sagemaker-runtime;savingsplans;schemas;sdb;secretsmanager;securityhub;serverlessrepo;servicecatalog;servicediscovery;service-quotas;sesv2;shield;signer;sms;sms-voice;snowball;sns;sqs;ssm;sso;sso-oidc;states;storagegateway;sts;support;swf;synthetics;textract;text-to-speech;transcribe;transcribestreaming;transfer;translate;waf;waf-regional;wafv2;workdocs;worklink;workmail;workmailmessageflow;workspaces;xray'
%else
%cmake \
    -DBUILD_SHARED_LIBS:BOOL=TRUE \
    -DBUILD_DEPS:BOOL=FALSE \
    -DAUTORUN_UNIT_TESTS:BOOL=FALSE \
    -DCUSTOM_MEMORY_MANAGEMENT:BOOL=FALSE \
    -DBUILD_ONLY='accessanalyzer;access-management;acm;acm-pca;alexaforbusiness;amplify;apigateway;apigatewaymanagementapi;apigatewayv2;appconfig;application-autoscaling;application-insights;appmesh;appstream;appsync;athena;autoscaling;autoscaling-plans;AWSMigrationHub;awstransfer;backup;batch;budgets;ce;chime;cloud9;clouddirectory;cloudformation;cloudfront;cloudhsm;cloudhsmv2;cloudsearch;cloudsearchdomain;cloudtrail;codeartifact;codebuild;codecommit;codedeploy;codeguruprofiler;codeguru-reviewer;codepipeline;codestar;codestar-connections;codestar-notifications;cognito-identity;cognito-idp;cognito-sync;comprehend;comprehendmedical;compute-optimizer;config;connect;connectparticipant;cur;dataexchange;datapipeline;datasync;dax;detective;devicefarm;directconnect;discovery;dlm;dms;docdb;ds;dynamodb;dynamodbstreams;ebs;ec2;ec2-instance-connect;ecr;ecs;eks;elasticache;elasticbeanstalk;elasticfilesystem;elastic-inference;elasticloadbalancing;elasticloadbalancingv2;elasticmapreduce;elastictranscoder;email;es;eventbridge;events;firehose;fms;forecast;forecastquery;frauddetector;gamelift;glacier;globalaccelerator;glue;greengrass;groundstation;guardduty;health;iam;identity-management;imagebuilder;importexport;inspector;iot;iot1click-devices;iot1click-projects;iotanalytics;iot-data;iotevents;iotevents-data;iot-jobs-data;iotsecuretunneling;iotsitewise;iotthingsgraph;kafka;kendra;kinesis;kinesisanalytics;kinesisanalyticsv2;kinesisvideo;kinesis-video-archived-media;kinesis-video-media;kinesis-video-signaling;kms;lakeformation;lambda;lex;lex-models;license-manager;lightsail;logs;machinelearning;macie;macie2;managedblockchain;marketplace-catalog;marketplacecommerceanalytics;marketplace-entitlement;mediaconnect;mediaconvert;medialive;mediapackage;mediapackage-vod;mediastore;mediastore-data;mediatailor;meteringmarketplace;migrationhub-config;mobile;mobileanalytics;monitoring;mq;mturk-requester;neptune;networkmanager;opsworks;opsworkscm;organizations;outposts;personalize;personalize-events;personalize-runtime;pi;pinpoint;pinpoint-email;polly;polly-sample;pricing;qldb;qldb-session;queues;quicksight;ram;rds;rds-data;redshift;rekognition;resource-groups;resourcegroupstaggingapi;robomaker;route53;route53domains;route53resolver;s3;s3control;s3-encryption;sagemaker;sagemaker-a2i-runtime;sagemaker-runtime;savingsplans;schemas;sdb;secretsmanager;securityhub;serverlessrepo;servicecatalog;servicediscovery;service-quotas;sesv2;shield;signer;sms;sms-voice;snowball;sns;sqs;ssm;sso;sso-oidc;states;storagegateway;sts;support;swf;synthetics;textract;text-to-speech;transcribe;transcribestreaming;transfer;translate;waf;waf-regional;wafv2;workdocs;worklink;workmail;workmailmessageflow;workspaces;xray'
%endif
make %{?_smp_mflags}

%install
%make_install

%check
%if 0%{?el7}
ctest3 -V %{?_smp_mflags}
%else
ctest -V %{?_smp_mflags}
%endif

%files
%{_libdir}/lib*.so

%files devel
%{_includedir}/aws
%{_libdir}/cmake
%{_libdir}/pkgconfig

%changelog
* Wed Jun 24 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.361-1
- Bump to 1.7.361
- Build everything except 'fsx' to work around a temporary build failue in that
  component

* Tue Jun 23 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.360-1
- Bump to 1.7.360

* Thu Jun 11 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.353-1
- Bump to 1.7.353

* Wed Jun 10 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.351-1
- Bump to 1.7.351
- Remove patch, that has been commited upstream

* Wed May 13 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.333-1
- Bump to 1.7.333

* Thu May 07 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.329-2
- Really apply patch

* Thu May 07 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.329-1
- Bump to 1.7.329, add patch for EPEL 7

* Wed May 06 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.328-1
- Bump to 1.7.328

* Sat May 02 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.326-1
- Bump to 1.7.326

* Thu Apr 30 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.324-1
- Bump to 1.7.324

* Wed Apr 29 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.323-1
- Bump to 1.7.323

* Tue Apr 28 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.322-1
- Bump to 1.7.322

* Sun Apr 26 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.321-1
- Bump to 1.7.321

* Fri Apr 24 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.320-1
- Bump to 1.7.320

* Thu Apr 23 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.319-1
- Bump to 1.7.319

* Mon Apr 20 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.316-1
- Bump to 1.7.316

* Thu Apr 16 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.314-2
- rebuilt

* Thu Apr 09 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.314-1
- Bump to 1.7.314

* Wed Apr 08 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.313-2
- Disable custom memory management

* Wed Apr 08 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.313-1
- Bump to 1.7.313

* Thu Apr 02 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.309-1
- Bump to 1.7.309

* Mon Mar 30 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.306-1
- Bump to 1.7.306

* Fri Mar 27 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.305-1
- Bump to 1.7.305

* Sat Mar 21 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.301-1
- Bump to 1.7.301

* Thu Mar 19 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.299-1
- Bump to 1.7.299

* Wed Mar 18 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.298-1
- Bump to 1.7.298

* Tue Mar 17 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.297-1
- Bump to 1.7.297

* Sun Mar 15 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.296-1
- Bump to 1.7.296

* Thu Mar 12 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.294-1
- Bump to 1.7.294
- Don't do a 'Release' build
- The cmake files in the devel package search for several packages. Account for
  this in the dependencies.

* Tue Mar 10 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.292-2
- Nuke compiler options '-Werror' and '-pedantic'

* Tue Mar 10 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.292-1
- Initial RPM release
