# QueryDsl이란?
- QueryDsl은 정적 타입을 이용해서 SQL과 같은 쿼리를 생성할 수 있도록 해주는 프레임워크이다.

# Gradle 설정

```
// QueryDSL 5.0이상 부터는 아래의 옵션을 추가해주시면 됩니다.
 plugins {
 	...
 	id "com.ewerk.gradle.plugins.querydsl" version "1.0.10"
 	...
 }
 ...
 dependencies {
 	// querydsl 추가
 	implementation "com.querydsl:querydsl-jpa:5.0.0"
 	implementation "com.querydsl:querydsl-apt:5.0.0"
     ...
 }
 // Qtype 생성 경로
 def querydslDir = "$buildDir/generated/querydsl"
 querydsl {
 	jpa = true
 	querydslSourcesDir = querydslDir
 }
 sourceSets {
 	main.java.srcDir querydslDir
 }
 compileQuerydsl{
 	options.annotationProcessorPath = configurations.querydsl
 }
 configurations {
 	compileOnly {
 		extendsFrom annotationProcessor
 	}
 	querydsl.extendsFrom compileClasspath
 }
```
