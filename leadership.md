# Leadership & Management Scenarios

## Scenario 1: Team Management

### Task Allocation Strategy

I would break the work into clear modules such as image processing, CSV handling, and UI. Tasks would be assigned based on strengths:

* Stronger developer: core processing logic
* Second developer: UI and integration
* Underperformer: smaller, well-defined tasks like logging, validation, or testing

Daily check-ins would be used to track progress and unblock issues quickly.

### Handling the Underperformer

I would first have a one-on-one discussion to understand if the issue is due to lack of clarity, skills, or motivation. Then I would:

* Assign smaller, clearly scoped tasks
* Provide guidance or pair programming if needed
* Monitor progress with short feedback loops

### Priority Trade-offs

* Focus on delivering a working MVP first
* Maintain quality in core functionality
* Avoid overloading high performers to protect team morale

---

## Scenario 2: Production Issue

### Immediate Actions (First Hour)

* Check logs and identify error patterns
* Pause or limit new jobs if needed
* Verify if the issue is related to recent deployment
* Roll back if necessary

### Debugging Approach

* Reproduce the issue in a controlled environment
* Isolate the failing component (API, processing, storage)
* Add temporary logging if required
* Fix root cause instead of applying temporary patches

### Stakeholder Communication

* Communicate impact clearly (e.g., percentage of failures)
* Provide estimated resolution time
* Share regular updates until resolved

---

## Scenario 3: Conflict Handling

I would allow both developers to present their viewpoints and reasoning. The decision would be based on:

* Scalability
* Team familiarity with the technology
* Project timeline

If needed, I would make the final decision to ensure progress, while explaining the reasoning to maintain transparency and team alignment.

---

# Code Review Approach

When reviewing code, I focus on:

### Issues Identified

* Lack of modular structure and separation of concerns
* Missing error handling and logging
* Inefficient processing (no parallelism or batching)
* Poor readability and naming conventions

### Suggested Improvements

* Refactor into smaller, reusable functions
* Introduce proper logging and retry mechanisms
* Improve performance using parallel processing
* Use clear and consistent naming conventions

---

# Communication to Non-Technical Stakeholders

This system automates the process of preparing product images for an online catalog.

Instead of manually editing each image, the system takes a folder of product photos and a spreadsheet with product details. It then automatically cleans the images, enhances their quality, and creates an additional styled version based on a selected theme.

This reduces manual effort, speeds up the workflow, and ensures consistent image quality across all products.
