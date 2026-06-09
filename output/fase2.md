# Compilación proyectos MIR

## Resumen Ejecutivo
- Total de proyectos: 548
- Total de proyectos de Casos de Uso: 405
- Total de proyectos MIR en uc: 121
- Proyectos activos (no deprecated): 77
- Proyectos que compilan correctamente: 45
- Tasa de éxito: 45/77 (58.4%)

## Proyectos que NO compilan
- gea-uc-mir-cdr-convergente
- gea-uc-mir-dp-mmt-workflows
- gea-uc-mir-dp-mobile-agents-workflows
- gea-uc-mir-dp-ret-ceres-workflows
- gea-uc-mir-dp-topology-norm-workflows
- gea-uc-mir-dp-traff-pic-workflows
- gea-uc-mir-dp-v360-workflows
- gea-uc-mir-ox-slpp
- gea-uc-mir-uc-baja-vol-workflows
- gea-uc-mir-uc-bat-jzz-workflows
- gea-uc-mir-uc-billing-shock-workflows
- gea-uc-mir-uc-cem-dq-workflows
- gea-uc-mir-uc-cem-science-workflows
- gea-uc-mir-uc-churn-jzz-workflows
- gea-uc-mir-uc-comm-kpi-workflows
- gea-uc-mir-uc-comm-workflows
- gea-uc-mir-uc-cust-profit-simu-workflows
- gea-uc-mir-uc-datashare-workflows
- gea-uc-mir-uc-dig-camp-enrich-cdp-workflows
- gea-uc-mir-uc-dig-camp-enrich-workflows
- gea-uc-mir-uc-digital-dat-workflows
- gea-uc-mir-uc-hera-offers-workflows
- gea-uc-mir-uc-minerva-workflows
- gea-uc-mir-uc-mmm-workflows
- gea-uc-mir-uc-nptb-jzz-workflows
- gea-uc-mir-uc-nptb-soho-workflows
- gea-uc-mir-uc-nptb-workflows
- gea-uc-mir-uc-ppool-workflows
- gea-uc-mir-uc-scx-workflows
- gea-uc-mir-uc-traff-growth-ingestion
- gea-uc-mir-uc09-sac-stats
- gea-uc-mir-uc30-rosetta-ingest

## Detalle de errores

### gea-uc-mir-cdr-convergente
```
Starting a Gradle Daemon (subsequent builds will be faster)


FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'cdr-convergente'.
> Could not resolve all artifacts for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.2.41.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.2.41.
         > Could not get resource 'https://torredecontrol.si.orange.es/nexus/repository/jcenter/org/jetbrains/kotlin/kotlin-gradle-plugin/1.2.41/kotlin-gradle-plugin-1.2.41.pom'.
            > Could not GET 'https://torredecontrol.si.orange.es/nexus/repository/jcenter/org/jetbrains/kotlin/kotlin-gradle-plugin/1.2.41/kotlin-gradle-plugin-1.2.41.pom'.
               > Connect to torredecontrol.si.orange.es:443 [torredecontrol.si.orange.es/10.113.58.155] failed: connect timed out

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 31s
```

### gea-uc-mir-dp-mmt-workflows
```
> Task :prepareDirs
> Task :jobs FAILED
2 actionable tasks: 2 executed


FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':jobs'.
> Could not resolve all files for configuration ':job'.
   > Could not resolve orange.bigdata.pat:mmt-jobs:2.4.0.
     Required by:
         project :
      > Could not resolve orange.bigdata.pat:mmt-jobs:2.4.0.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/geaosp-group/orange/bigdata/pat/mmt-jobs/2.4.0/mmt-jobs-2.4.0.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/geaosp-group/orange/bigdata/pat/mmt-jobs/2.4.0/mmt-jobs-2.4.0.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es: nodename nor servname provided, or not known
      > Could not resolve orange.bigdata.pat:mmt-jobs:2.4.0.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/orange/bigdata/pat/mmt-jobs/2.4.0/mmt-jobs-2.4.0.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/orange/bigdata/pat/mmt-jobs/2.4.0/mmt-jobs-2.4.0.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 525ms
```

### gea-uc-mir-dp-mobile-agents-workflows
```
Downloading https://services.gradle.org/distributions/gradle-5.4.1-bin.zip
...................................................................................

Welcome to Gradle 5.4.1!

Here are the highlights of this release:
 - Run builds with JDK12
 - New API for Incremental Tasks
 - Updates to native projects, including Swift 5 support

For more details see https://docs.gradle.org/5.4.1/release-notes.html

Starting a Gradle Daemon (subsequent builds will be faster)

Deprecated Gradle features were used in this build, making it incompatible with Gradle 6.0.
Use '--warning-mode all' to show the individual deprecation warnings.
See https://docs.gradle.org/5.4.1/userguide/command_line_interface.html#sec:command_line_warnings


FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'mobile_agents_workflows'.
> Could not resolve all artifacts for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.4.32.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.4.32.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.4.32/kotlin-gradle-plugin-1.4.32.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.4.32/kotlin-gradle-plugin-1.4.32.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es: nodename nor servname provided, or not known

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 10s
```

### gea-uc-mir-dp-ret-ceres-workflows
```
FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'ret_ceres_workflows'.
> Could not resolve all artifacts for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es: nodename nor servname provided, or not known

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 1s
```

### gea-uc-mir-dp-topology-norm-workflows
```
FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'topology_norm_workflows'.
> Could not resolve all artifacts for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.61.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.61.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.61/kotlin-gradle-plugin-1.3.61.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.61/kotlin-gradle-plugin-1.3.61.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es: nodename nor servname provided, or not known

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 0s
```

### gea-uc-mir-dp-traff-pic-workflows
```
> Task :prepareDirs
> Task :jobs FAILED
2 actionable tasks: 2 executed


FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':jobs'.
> Could not resolve all files for configuration ':job'.
   > Could not resolve orange.bigdata.pat:traff_pic_jobs:2.0.1.
     Required by:
         project :
      > Could not resolve orange.bigdata.pat:traff_pic_jobs:2.0.1.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/geaosp-group/orange/bigdata/pat/traff_pic_jobs/2.0.1/traff_pic_jobs-2.0.1.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/geaosp-group/orange/bigdata/pat/traff_pic_jobs/2.0.1/traff_pic_jobs-2.0.1.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es: nodename nor servname provided, or not known
      > Could not resolve orange.bigdata.pat:traff_pic_jobs:2.0.1.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/orange/bigdata/pat/traff_pic_jobs/2.0.1/traff_pic_jobs-2.0.1.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/orange/bigdata/pat/traff_pic_jobs/2.0.1/traff_pic_jobs-2.0.1.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 453ms
```

### gea-uc-mir-dp-v360-workflows
```
> Configure project :
Configuring credentials for repo: https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-group/...
Configuring credentials for repo: https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-thirdparties/...

> Task :prepareDirs
> Task :jobs
> Task :jobs FAILED
2 actionable tasks: 2 executed


FAILURE: Build failed with an exception.

* Where:
Script '/Users/miqui/git/github/miqui-infante/test-migration/tmp/gea-uc-mir-dp-v360-workflows/gradle/distribution.gradle' line: 44

* What went wrong:
Could not resolve all files for configuration ':job'.
> Could not download v360_normalization-1.27.3.jar (orange.bigdata.pat:v360_normalization:1.27.3)
   > Could not get resource 'https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-group/orange/bigdata/pat/v360_normalization/1.27.3/v360_normalization-1.27.3.jar'.
      > Could not GET 'https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-group/orange/bigdata/pat/v360_normalization/1.27.3/v360_normalization-1.27.3.jar'.
         > Read timed out

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 1m 35s
```

### gea-uc-mir-ox-slpp
```
Downloading https://services.gradle.org/distributions/gradle-3.5.1-bin.zip
.................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................
Unzipping /Users/miqui/.gradle/wrapper/dists/gradle-3.5.1-bin/5aglzaqc99i3lll5iwkbm96su/gradle-3.5.1-bin.zip to /Users/miqui/.gradle/wrapper/dists/gradle-3.5.1-bin/5aglzaqc99i3lll5iwkbm96su
Set executable permissions for: /Users/miqui/.gradle/wrapper/dists/gradle-3.5.1-bin/5aglzaqc99i3lll5iwkbm96su/gradle-3.5.1/bin/gradle
Starting a Gradle Daemon (subsequent builds will be faster)

BUILD FAILED

Total time: 1 mins 24.779 secs


FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'ox_slpp'.
> Could not resolve all dependencies for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.2.41.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.2.41.
         > Could not get resource 'https://torredecontrol.si.orange.es/nexus/repository/jcenter/org/jetbrains/kotlin/kotlin-gradle-plugin/1.2.41/kotlin-gradle-plugin-1.2.41.pom'.
            > Could not GET 'https://torredecontrol.si.orange.es/nexus/repository/jcenter/org/jetbrains/kotlin/kotlin-gradle-plugin/1.2.41/kotlin-gradle-plugin-1.2.41.pom'.
               > Connect to torredecontrol.si.orange.es:443 [torredecontrol.si.orange.es/10.113.58.155] failed: Operation timed out (Connection timed out)

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output.
```

### gea-uc-mir-uc-baja-vol-workflows
```
FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'baja_vol_workflows'.
> Could not resolve all artifacts for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es: nodename nor servname provided, or not known

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 0s
```

### gea-uc-mir-uc-bat-jzz-workflows
```
> Task :prepareDirs
> Task :jobs FAILED

Deprecated Gradle features were used in this build, making it incompatible with Gradle 8.0.

You can use '--warning-mode all' to show the individual deprecation warnings and determine if they come from your own scripts or plugins.

See https://docs.gradle.org/7.4.2/userguide/command_line_interface.html#sec:command_line_warnings
2 actionable tasks: 2 executed


FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':jobs'.
> Could not resolve all files for configuration ':job'.
   > Could not resolve orange.bigdata.mkt:bat_jzz_jobs:2.5.1.
     Required by:
         project :
      > Could not resolve orange.bigdata.mkt:bat_jzz_jobs:2.5.1.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/geaosp-group/orange/bigdata/mkt/bat_jzz_jobs/2.5.1/bat_jzz_jobs-2.5.1.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/geaosp-group/orange/bigdata/mkt/bat_jzz_jobs/2.5.1/bat_jzz_jobs-2.5.1.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es: nodename nor servname provided, or not known
      > Could not resolve orange.bigdata.mkt:bat_jzz_jobs:2.5.1.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/orange/bigdata/mkt/bat_jzz_jobs/2.5.1/bat_jzz_jobs-2.5.1.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/orange/bigdata/mkt/bat_jzz_jobs/2.5.1/bat_jzz_jobs-2.5.1.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 2s
```

### gea-uc-mir-uc-billing-shock-workflows
```
> Task :prepareDirs
> Task :jobs FAILED
2 actionable tasks: 2 executed


FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':jobs'.
> Could not resolve all files for configuration ':job'.
   > Could not resolve orange.bigdata.sac:billing_shock_jobs:1.6.0.
     Required by:
         project :
      > Could not resolve orange.bigdata.sac:billing_shock_jobs:1.6.0.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/orange/bigdata/sac/billing_shock_jobs/1.6.0/billing_shock_jobs-1.6.0.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/orange/bigdata/sac/billing_shock_jobs/1.6.0/billing_shock_jobs-1.6.0.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es
      > Could not resolve orange.bigdata.sac:billing_shock_jobs:1.6.0.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/geaosp-group/orange/bigdata/sac/billing_shock_jobs/1.6.0/billing_shock_jobs-1.6.0.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/geaosp-group/orange/bigdata/sac/billing_shock_jobs/1.6.0/billing_shock_jobs-1.6.0.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 460ms
```

### gea-uc-mir-uc-cem-dq-workflows
```
Deprecated Gradle features were used in this build, making it incompatible with Gradle 6.0.
Use '--warning-mode all' to show the individual deprecation warnings.
See https://docs.gradle.org/5.4.1/userguide/command_line_interface.html#sec:command_line_warnings


FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'cem_dq_workflows'.
> Could not resolve all artifacts for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es: nodename nor servname provided, or not known

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 1s
```

### gea-uc-mir-uc-cem-science-workflows
```
Downloading https://services.gradle.org/distributions/gradle-5.6.4-all.zip
.............10%.............20%.............30%..............40%.............50%.............60%..............70%.............80%.............90%..............100%

Welcome to Gradle 5.6.4!

Here are the highlights of this release:
 - Incremental Groovy compilation
 - Groovy compile avoidance
 - Test fixtures for Java projects
 - Manage plugin versions via settings script

For more details see https://docs.gradle.org/5.6.4/release-notes.html

Starting a Gradle Daemon (subsequent builds will be faster)


FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'cem_science_workflows'.
> Could not resolve all artifacts for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.4.32.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.4.32.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.4.32/kotlin-gradle-plugin-1.4.32.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.4.32/kotlin-gradle-plugin-1.4.32.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es: nodename nor servname provided, or not known

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 15s
```

### gea-uc-mir-uc-churn-jzz-workflows
```
Initialized native services in: /Users/miqui/.gradle/native
The client will now receive all logging from the daemon (pid: 6067). The daemon log file: /Users/miqui/.gradle/daemon/4.10.3/daemon-6067.out.log
Starting 5th build in daemon [uptime: 46 mins 52.943 secs, performance: 100%]
Using 14 worker leases.
Starting Build
Compiling settings file '/Users/miqui/git/github/miqui-infante/test-migration/tmp/gea-uc-mir-uc-churn-jzz-workflows/settings.gradle' using SubsetScriptTransformer.
Compiling settings file '/Users/miqui/git/github/miqui-infante/test-migration/tmp/gea-uc-mir-uc-churn-jzz-workflows/settings.gradle' using BuildScriptTransformer.
Settings evaluated using settings file '/Users/miqui/git/github/miqui-infante/test-migration/tmp/gea-uc-mir-uc-churn-jzz-workflows/settings.gradle'.
Projects loaded. Root project using build file '/Users/miqui/git/github/miqui-infante/test-migration/tmp/gea-uc-mir-uc-churn-jzz-workflows/build.gradle'.
Included projects: [root project 'churn_jzz_workflows']

> Configure project :
Evaluating root project 'churn_jzz_workflows' using build file '/Users/miqui/git/github/miqui-infante/test-migration/tmp/gea-uc-mir-uc-churn-jzz-workflows/build.gradle'.
Compiling build file '/Users/miqui/git/github/miqui-infante/test-migration/tmp/gea-uc-mir-uc-churn-jzz-workflows/build.gradle' using SubsetScriptTransformer.


FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'churn_jzz_workflows'.
> Could not resolve all artifacts for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es: nodename nor servname provided, or not known

* Try:
Run with --stacktrace option to get the stack trace. Run with --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 0s
```

### gea-uc-mir-uc-comm-kpi-workflows
```
> Configure project :
Configuring credentials for repo: https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-group/...
Configuring credentials for repo: https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-thirdparties/...

> Task :prepareDirs
> Task :jobs
> Task :jobs FAILED

Deprecated Gradle features were used in this build, making it incompatible with Gradle 8.0.

You can use '--warning-mode all' to show the individual deprecation warnings and determine if they come from your own scripts or plugins.

See https://docs.gradle.org/7.4.2/userguide/command_line_interface.html#sec:command_line_warnings
2 actionable tasks: 2 executed


FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':jobs'.
> Could not resolve all files for configuration ':job'.
   > Could not download comm_kpi_calculator-3.1.1-all.jar (orange.bigdata.sac:comm_kpi_calculator:3.1.1)
      > Could not get resource 'https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-group/orange/bigdata/sac/comm_kpi_calculator/3.1.1/comm_kpi_calculator-3.1.1-all.jar'.
         > Could not GET 'https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-group/orange/bigdata/sac/comm_kpi_calculator/3.1.1/comm_kpi_calculator-3.1.1-all.jar'.
            > Read timed out

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 1m 36s
```

### gea-uc-mir-uc-comm-workflows
```
> Configure project :
Configuring credentials for repo: https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-group/...
Configuring credentials for repo: https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-thirdparties/...

> Task :prepareDirs
> Task :jobs
> Task :jobs FAILED
2 actionable tasks: 2 executed


FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':jobs'.
> Could not resolve all files for configuration ':job'.
   > Could not download comm_deduplication-1.2.2.jar (orange.bigdata.sac:comm_deduplication:1.2.2)
      > Could not get resource 'https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-group/orange/bigdata/sac/comm_deduplication/1.2.2/comm_deduplication-1.2.2.jar'.
         > Could not GET 'https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-group/orange/bigdata/sac/comm_deduplication/1.2.2/comm_deduplication-1.2.2.jar'.
            > Read timed out
   > Could not download comm_rep-1.3.1.jar (orange.bigdata.sac:comm_rep:1.3.1)
      > Could not get resource 'https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-group/orange/bigdata/sac/comm_rep/1.3.1/comm_rep-1.3.1.jar'.
         > Could not GET 'https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-group/orange/bigdata/sac/comm_rep/1.3.1/comm_rep-1.3.1.jar'.
            > Read timed out

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 1m 36s
```

### gea-uc-mir-uc-cust-profit-simu-workflows
```
Downloading https://services.gradle.org/distributions/gradle-5.2.1-bin.zip
...................................................................................

Welcome to Gradle 5.2.1!

Here are the highlights of this release:
 - Define sets of dependencies that work together with Java Platform plugin
 - New C++ plugins with dependency management built-in
 - New C++ project types for gradle init
 - Service injection into plugins and project extensions

For more details see https://docs.gradle.org/5.2.1/release-notes.html

Starting a Gradle Daemon (subsequent builds will be faster)

Deprecated Gradle features were used in this build, making it incompatible with Gradle 6.0.
Use '--warning-mode all' to show the individual deprecation warnings.
See https://docs.gradle.org/5.2.1/userguide/command_line_interface.html#sec:command_line_warnings


FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'cust_profit_simu_workflows'.
> Could not resolve all artifacts for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es: nodename nor servname provided, or not known

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 10s
```

### gea-uc-mir-uc-datashare-workflows
```
FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'datashare_workflows'.
> Could not resolve all artifacts for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es: nodename nor servname provided, or not known

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 0s
```

### gea-uc-mir-uc-dig-camp-enrich-cdp-workflows
```
Downloading https://services.gradle.org/distributions/gradle-6.2.2-bin.zip
.........10%.........20%.........30%..........40%.........50%.........60%..........70%.........80%.........90%..........100%

Welcome to Gradle 6.2.2!

Here are the highlights of this release:
 - Dependency checksum and signature verification
 - Shareable read-only dependency cache
 - Documentation links in deprecation messages

For more details see https://docs.gradle.org/6.2.2/release-notes.html

Starting a Gradle Daemon (subsequent builds will be faster)


FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'dig_camp_enrich_cdp_workflows'.
> Could not resolve all artifacts for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.61.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.61.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.61/kotlin-gradle-plugin-1.3.61.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.61/kotlin-gradle-plugin-1.3.61.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es: nodename nor servname provided, or not known

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 10s
```

### gea-uc-mir-uc-dig-camp-enrich-workflows
```
FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'dig_camp_enrich_workflows'.
> Could not resolve all artifacts for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.61.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.61.
         > Could not get resource 'https://torredecontrol.si.orange.es/nexus/repository/jcenter/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.61/kotlin-gradle-plugin-1.3.61.pom'.
            > Could not GET 'https://torredecontrol.si.orange.es/nexus/repository/jcenter/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.61/kotlin-gradle-plugin-1.3.61.pom'.
               > Connect to torredecontrol.si.orange.es:443 [torredecontrol.si.orange.es/10.113.58.155] failed: connect timed out

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 1m 33s
```

### gea-uc-mir-uc-digital-dat-workflows
```
Downloading https://services.gradle.org/distributions/gradle-4.4-bin.zip
........................................................................
Unzipping /Users/miqui/.gradle/wrapper/dists/gradle-4.4-bin/bgaq7vklkazwgxox0hdadxbvi/gradle-4.4-bin.zip to /Users/miqui/.gradle/wrapper/dists/gradle-4.4-bin/bgaq7vklkazwgxox0hdadxbvi
Set executable permissions for: /Users/miqui/.gradle/wrapper/dists/gradle-4.4-bin/bgaq7vklkazwgxox0hdadxbvi/gradle-4.4/bin/gradle
Starting a Gradle Daemon (subsequent builds will be faster)


FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'leadscore_workflows'.
> Could not resolve all files for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
         > Could not get resource 'https://torredecontrol.si.orange.es/nexus/repository/jcenter/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
            > Could not GET 'https://torredecontrol.si.orange.es/nexus/repository/jcenter/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
               > Connect to torredecontrol.si.orange.es:443 [torredecontrol.si.orange.es/10.113.58.155] failed: connect timed out

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 39s
```

### gea-uc-mir-uc-hera-offers-workflows
```
> Configure project :
Configuring credentials for repo: https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-group/...
Configuring credentials for repo: https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-thirdparties/...

> Task :prepareDirs
> Task :conns
> Task :jobs
> Task :jobs FAILED
3 actionable tasks: 3 executed


FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':jobs'.
> Could not resolve all files for configuration ':job'.
   > Could not download orange-hera-offers-jobs-1.3.0.jar (orange.bigdata:orange-hera-offers-jobs:1.3.0)
      > Could not get resource 'https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-group/orange/bigdata/orange-hera-offers-jobs/1.3.0/orange-hera-offers-jobs-1.3.0.jar'.
         > Could not GET 'https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-group/orange/bigdata/orange-hera-offers-jobs/1.3.0/orange-hera-offers-jobs-1.3.0.jar'.
            > Read timed out

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 1m 36s
```

### gea-uc-mir-uc-minerva-workflows
```
Downloading https://services.gradle.org/distributions/gradle-5.6.2-all.zip
.............10%.............20%.............30%..............40%.............50%.............60%..............70%.............80%.............90%..............100%

Welcome to Gradle 5.6.2!

Here are the highlights of this release:
 - Incremental Groovy compilation
 - Groovy compile avoidance
 - Test fixtures for Java projects
 - Manage plugin versions via settings script

For more details see https://docs.gradle.org/5.6.2/release-notes.html

Starting a Gradle Daemon (subsequent builds will be faster)
> Task :prepareDirs
> Task :jobs FAILED
2 actionable tasks: 2 executed


FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':jobs'.
> Could not resolve all files for configuration ':job'.
   > Could not resolve orange.bigdata.mkt:minerva_jobs:1.0.0.
     Required by:
         project :
      > Could not resolve orange.bigdata.mkt:minerva_jobs:1.0.0.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/geaosp-group/orange/bigdata/mkt/minerva_jobs/1.0.0/minerva_jobs-1.0.0.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/geaosp-group/orange/bigdata/mkt/minerva_jobs/1.0.0/minerva_jobs-1.0.0.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es: nodename nor servname provided, or not known
      > Could not resolve orange.bigdata.mkt:minerva_jobs:1.0.0.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/orange/bigdata/mkt/minerva_jobs/1.0.0/minerva_jobs-1.0.0.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/orange/bigdata/mkt/minerva_jobs/1.0.0/minerva_jobs-1.0.0.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 24s
```

### gea-uc-mir-uc-mmm-workflows
```
> Task :prepareDirs
> Task :jobs FAILED
2 actionable tasks: 2 executed


FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':jobs'.
> Could not resolve all files for configuration ':job'.
   > Could not resolve orange.bigdata.mkt:mmm_jobs:1.0.25.
     Required by:
         project :
      > Could not resolve orange.bigdata.mkt:mmm_jobs:1.0.25.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/geaosp-group/orange/bigdata/mkt/mmm_jobs/1.0.25/mmm_jobs-1.0.25.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/geaosp-group/orange/bigdata/mkt/mmm_jobs/1.0.25/mmm_jobs-1.0.25.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es: nodename nor servname provided, or not known
      > Could not resolve orange.bigdata.mkt:mmm_jobs:1.0.25.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/orange/bigdata/mkt/mmm_jobs/1.0.25/mmm_jobs-1.0.25.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/orange/bigdata/mkt/mmm_jobs/1.0.25/mmm_jobs-1.0.25.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 560ms
```

### gea-uc-mir-uc-nptb-jzz-workflows
```
Starting a Gradle Daemon (subsequent builds will be faster)


FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'nptb_jzz_workflows'.
> Could not resolve all files for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.4.32.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.4.32.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.4.32/kotlin-gradle-plugin-1.4.32.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.4.32/kotlin-gradle-plugin-1.4.32.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es: nodename nor servname provided, or not known

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 3s
```

### gea-uc-mir-uc-nptb-soho-workflows
```
Downloading https://services.gradle.org/distributions/gradle-4.10.3-all.zip
........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................
Unzipping /Users/miqui/.gradle/wrapper/dists/gradle-4.10.3-all/81msde2dx9p4vji0mjgtvxkcb/gradle-4.10.3-all.zip to /Users/miqui/.gradle/wrapper/dists/gradle-4.10.3-all/81msde2dx9p4vji0mjgtvxkcb
Set executable permissions for: /Users/miqui/.gradle/wrapper/dists/gradle-4.10.3-all/81msde2dx9p4vji0mjgtvxkcb/gradle-4.10.3/bin/gradle


FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'nptbsoho_workflows'.
> Could not resolve all artifacts for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
            > Could not HEAD 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es: nodename nor servname provided, or not known

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 12s
```

### gea-uc-mir-uc-nptb-workflows
```
FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'nptb_workflows'.
> Could not resolve all artifacts for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.2.41.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.2.41.
         > Could not get resource 'https://torredecontrol.si.orange.es/nexus/repository/jcenter/org/jetbrains/kotlin/kotlin-gradle-plugin/1.2.41/kotlin-gradle-plugin-1.2.41.pom'.
            > Could not GET 'https://torredecontrol.si.orange.es/nexus/repository/jcenter/org/jetbrains/kotlin/kotlin-gradle-plugin/1.2.41/kotlin-gradle-plugin-1.2.41.pom'.
               > Connect to torredecontrol.si.orange.es:443 [torredecontrol.si.orange.es/10.113.58.155] failed: connect timed out

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 30s
```

### gea-uc-mir-uc-ppool-workflows
```
Downloading https://services.gradle.org/distributions/gradle-5.3-all.zip
..................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................
Unzipping /Users/miqui/.gradle/wrapper/dists/gradle-5.3-all/a2o9bs8pjyp10tdbmwhtqkmvn/gradle-5.3-all.zip to /Users/miqui/.gradle/wrapper/dists/gradle-5.3-all/a2o9bs8pjyp10tdbmwhtqkmvn
Set executable permissions for: /Users/miqui/.gradle/wrapper/dists/gradle-5.3-all/a2o9bs8pjyp10tdbmwhtqkmvn/gradle-5.3/bin/gradle

Welcome to Gradle 5.3!

Here are the highlights of this release:
 - Feature variants AKA "optional dependencies"
 - Type-safe accessors in Kotlin precompiled script plugins
 - Gradle Module Metadata 1.0

For more details see https://docs.gradle.org/5.3/release-notes.html

Starting a Gradle Daemon (subsequent builds will be faster)


FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'ppool_workflows'.
> Could not resolve all artifacts for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
            > Could not HEAD 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es: nodename nor servname provided, or not known

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 17s
```

### gea-uc-mir-uc-scx-workflows
```
FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'SCX_workflows'.
> Could not resolve all artifacts for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.50.
         > Could not get resource 'https://torredecontrol.si.orange.es/nexus/repository/jcenter/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
            > Could not HEAD 'https://torredecontrol.si.orange.es/nexus/repository/jcenter/org/jetbrains/kotlin/kotlin-gradle-plugin/1.3.50/kotlin-gradle-plugin-1.3.50.pom'.
               > Connect to torredecontrol.si.orange.es:443 [torredecontrol.si.orange.es/10.113.58.155] failed: connect timed out

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 30s
```

### gea-uc-mir-uc-traff-growth-ingestion
```
FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'traff_growth_ingestion'.
> Could not resolve all files for configuration ':classpath'.
   > Could not download kotlin-stdlib-1.3.50.jar (org.jetbrains.kotlin:kotlin-stdlib:1.3.50)
      > Could not get resource 'https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-thirdparties/org/jetbrains/kotlin/kotlin-stdlib/1.3.50/kotlin-stdlib-1.3.50.jar'.
         > Could not HEAD 'https://europe-maven.pkg.dev/osp-gea-prod/gea-maven-thirdparties/org/jetbrains/kotlin/kotlin-stdlib/1.3.50/kotlin-stdlib-1.3.50.jar'. Received status code 401 from server: Unauthorized

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 4s
```

### gea-uc-mir-uc09-sac-stats
```
Downloading https://services.gradle.org/distributions/gradle-5.3.1-bin.zip
...................................................................................

Welcome to Gradle 5.3.1!

Here are the highlights of this release:
 - Feature variants AKA "optional dependencies"
 - Type-safe accessors in Kotlin precompiled script plugins
 - Gradle Module Metadata 1.0

For more details see https://docs.gradle.org/5.3.1/release-notes.html

Starting a Gradle Daemon (subsequent builds will be faster)


FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'cj_stats_wf'.
> Could not resolve all artifacts for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.2.51.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.2.51.
         > Could not get resource 'https://torredecontrol.si.orange.es/nexus/repository/jcenter/org/jetbrains/kotlin/kotlin-gradle-plugin/1.2.51/kotlin-gradle-plugin-1.2.51.pom'.
            > Could not GET 'https://torredecontrol.si.orange.es/nexus/repository/jcenter/org/jetbrains/kotlin/kotlin-gradle-plugin/1.2.51/kotlin-gradle-plugin-1.2.51.pom'.
               > Connect to torredecontrol.si.orange.es:443 [torredecontrol.si.orange.es/10.113.58.155] failed: connect timed out

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 1m 44s
```

### gea-uc-mir-uc30-rosetta-ingest
```
Downloading https://services.gradle.org/distributions/gradle-4.0-bin.zip
................................................................
Unzipping /Users/miqui/.gradle/wrapper/dists/gradle-4.0-bin/3p92xsbhik5vmig8i90n16yxc/gradle-4.0-bin.zip to /Users/miqui/.gradle/wrapper/dists/gradle-4.0-bin/3p92xsbhik5vmig8i90n16yxc
Set executable permissions for: /Users/miqui/.gradle/wrapper/dists/gradle-4.0-bin/3p92xsbhik5vmig8i90n16yxc/gradle-4.0/bin/gradle
Starting a Gradle Daemon (subsequent builds will be faster)


FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'ingestas_rosetta'.
> Could not resolve all files for configuration ':classpath'.
   > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.2.41.
     Required by:
         project :
      > Could not resolve org.jetbrains.kotlin:kotlin-gradle-plugin:1.2.41.
         > Could not get resource 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.2.41/kotlin-gradle-plugin-1.2.41.pom'.
            > Could not GET 'https://artifactsrepository-tc.shared-nonprod.cloud.si.orange.es/artifactory/jcenter-TC3/org/jetbrains/kotlin/kotlin-gradle-plugin/1.2.41/kotlin-gradle-plugin-1.2.41.pom'.
               > artifactsrepository-tc.shared-nonprod.cloud.si.orange.es: nodename nor servname provided, or not known

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output.

BUILD FAILED in 10s
```

