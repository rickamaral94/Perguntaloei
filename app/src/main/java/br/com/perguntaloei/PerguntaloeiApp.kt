package br.com.perguntaloei

import android.app.Application
import br.com.perguntaloei.diag.Diagnostics

class PerguntaloeiApp : Application() {
    override fun onCreate() {
        super.onCreate()
        Diagnostics.init(this, BuildConfig.VERSION_NAME)
    }
}
