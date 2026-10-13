# kotlinx.serialization
-keepattributes *Annotation*, InnerClasses
-dontnote kotlinx.serialization.**
-keepclassmembers class kotlinx.serialization.json.** { *** Companion; }
-keepclasseswithmembers class kotlinx.serialization.json.** { kotlinx.serialization.KSerializer serializer(...); }
-keep,includedescriptorclasses class br.com.perguntaloei.**$$serializer { *; }
-keepclassmembers class br.com.perguntaloei.** { *** Companion; }
-keepclasseswithmembers class br.com.perguntaloei.** { kotlinx.serialization.KSerializer serializer(...); }

# sherpa-onnx (voz neural): o código nativo acessa estas classes e campos por nome.
-keep class com.k2fsa.sherpa.onnx.** { *; }
