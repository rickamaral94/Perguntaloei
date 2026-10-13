pluginManagement {
    repositories {
        google()
        // Espelho do Maven Central mantido pelo Google (evita limite de requisições do repo1).
        maven("https://maven-central.storage-download.googleapis.com/maven2/")
        mavenCentral()
        gradlePluginPortal()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        // Espelho do Maven Central mantido pelo Google (evita limite de requisições do repo1).
        maven("https://maven-central.storage-download.googleapis.com/maven2/")
        mavenCentral()
    }
}
rootProject.name = "Perguntaloei"
include(":app")
