library(openxlsx)

# Read the Excel file
pkg_data <- read.xlsx("Rlinux_processed.xlsx", colNames = TRUE)

# Ensure there is a column specifying users
if (!"User" %in% colnames(pkg_data) || !"Package" %in% colnames(pkg_data)) {
  stop("The Excel file must contain 'User' and 'Package' columns.")
}

# Create directories and write individual requirements files
unique_users <- unique(pkg_data$User)

for (user in unique_users) {
  user_dir <- file.path(getwd(), user)
  if (!dir.exists(user_dir)) {
    dir.create(user_dir)
  }
  
  user_packages <- pkg_data$Package[pkg_data$User == user]
  writeLines(user_packages, file.path(user_dir, "requirements_rlinux.txt"))
}

cat("User-specific requirements files generated successfully.\n")