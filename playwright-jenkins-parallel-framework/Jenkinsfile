pipeline {
    agent none // We don't allocate a global agent, we use specific nodes in steps

    stages {
        stage('Parallel Test Execution') {
            parallel {
                stage('Node 1 - Login Tests') {
                    agent {
                        label 'playwright-node-1'
                    }
                    steps {
                        // Stage 1: Checkout
                        checkout scm
                        
                        // Stage 2: Install dependencies
                        sh 'pip install -r requirements.txt'
                        
                        // Stage 3: Install Playwright browsers
                        sh 'playwright install chromium'
                        
                        // Stage 4: Run Tests
                        sh 'pytest tests/test_login.py --junitxml=results-login.xml'
                    }
                    post {
                        always {
                            junit 'results-login.xml'
                            archiveArtifacts artifacts: 'test-results/**/*', allowEmptyArchive: true
                        }
                    }
                }
                
                stage('Node 2 - Cart & Checkout Tests') {
                    agent {
                        label 'playwright-node-2'
                    }
                    steps {
                        // Stage 1: Checkout
                        checkout scm
                        
                        // Stage 2: Install dependencies
                        sh 'pip install -r requirements.txt'
                        
                        // Stage 3: Install Playwright browsers
                        sh 'playwright install chromium'
                        
                        // Stage 4: Run Tests
                        sh 'pytest tests/test_cart.py tests/test_checkout.py --junitxml=results-cart-checkout.xml'
                    }
                    post {
                        always {
                            junit 'results-cart-checkout.xml'
                            archiveArtifacts artifacts: 'test-results/**/*', allowEmptyArchive: true
                        }
                    }
                }
            }
        }
    }
}
