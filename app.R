library(shiny)
library(ggplot2)
library(dplyr)

# The User Interface (UI)
ui <- fluidPage(
  titlePanel("Analytical-Minds' Enterprise-Scale Fraud Analytics Dashboard"),
  
  sidebarLayout(
    sidebarPanel(
      h4("Security Control Panel"),
      helpText("Interact with the Big Data insights processed via Spark and R."),
      hr(),
      selectInput("type_select", "Select Transaction Vector:", 
                  choices = unique(df$type), selected = "TRANSFER"),
      
      sliderInput("amt_slider", "Set Amount Threshold:", 
                  min = 0, max = 1000000, value = 250000),
      
      hr(),
      h5("Model Metadata"),
      p("Algorithm: Decision Tree (RPART)"),
      p("Accuracy: 99.79%")
    ),
    
    mainPanel(
      tabsetPanel(
        tabPanel("Risk Distribution", 
                 plotOutput("fraudPlot"),
                 br(),
                 h4("Transaction Volume Summary"),
                 tableOutput("summaryTable")),
        tabPanel("ML Insights", 
                 h4("Predictive Logic Summary"),
                 p("The dashboard visualizes how the Decision Tree handles different transaction volumes."),
                 verbatimTextOutput("treeStats"))
      )
    )
  )
)

# The Server Logic
server <- function(input, output) {
  
  filtered_data <- reactive({
    df %>% 
      filter(type == input$type_select, 
             amount <= input$amt_slider)
  })
  
  output$fraudPlot <- renderPlot({
    ggplot(filtered_data(), aes(x = amount, fill = as.factor(isFraud))) +
      geom_histogram(bins = 30, alpha = 0.8, color = "white") +
      scale_fill_manual(values = c("0" = "#2c3e50", "1" = "#e74c3c"), 
                        name = "Fraud Status (1=Fraud)") +
      theme_minimal() +
      labs(title = paste("Risk Density for", input$type_select, "Transactions"),
           x = "Transaction Amount", y = "Frequency of Events")
  })
  
  output$summaryTable <- renderTable({
    filtered_data() %>%
      group_by(isFraud) %>%
      summarise(Count = n(), 
                Avg_Amount = mean(amount), 
                Max_Amount = max(amount))
  })
  
  output$treeStats <- renderPrint({
    print(fraud_tree)
  })
}

# Launch the Application
shinyApp(ui = ui, server = server)