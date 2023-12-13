import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

class BreastCancerClassifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Breast Cancer Classifier")

        # Create and set up the main frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        # Add widgets to the frame
        self.file_label = ttk.Label(self.main_frame, text="Select CSV File:")
        self.file_label.grid(column=0, row=0, sticky=tk.W)

        self.file_entry = ttk.Entry(self.main_frame, width=40, state='readonly')
        self.file_entry.grid(column=0, row=1, sticky=(tk.W, tk.E))

        self.browse_button = ttk.Button(self.main_frame, text="Browse", command=self.browse_file)
        self.browse_button.grid(column=1, row=1, sticky=tk.W)

        self.predict_button = ttk.Button(self.main_frame, text="Predict", command=self.predict)
        self.predict_button.grid(column=0, row=2, sticky=tk.W)

        # Initialize classifier and other variables
        self.classifier = None
        self.scaler = None
        self.pca = None

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)

            # Load the data and train the classifier
            try:
                df = pd.read_csv(file_path)
                print("Loaded Data:")
                print(df.head())

                # Set y directly as the target labels
                y = df["diagnosis"]
                X = df.drop("diagnosis", axis=1)

                # Split the data for training and testing
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                # Preprocess data
                self.scaler = StandardScaler()
                X_train_scaled = self.scaler.fit_transform(X_train)
                X_test_scaled = self.scaler.transform(X_test)

                # Apply PCA
                self.pca = PCA(n_components=2)
                X_train_pca = self.pca.fit_transform(X_train_scaled)
                X_test_pca = self.pca.transform(X_test_scaled)

                # Train the classifier
                self.classifier = SVC(probability=True)
                self.classifier.fit(X_train_pca, y_train)
            except Exception as e:
                messagebox.showerror("Error", f"Error loading data: {e}")

    def predict(self):
        if self.classifier is not None:
            if not hasattr(self, 'scaler') or not hasattr(self, 'pca'):
                messagebox.showerror("Error", "Please browse and load a CSV file first.")
                return

            # Placeholder for input data, replace it with your actual input data
            X_input = pd.DataFrame({
                'radius_mean': [14.02],
                'texture_mean': [15.66],
                'perimeter_mean': [89.59],
                'area_mean': [606.5],
                'smoothness_mean': [0.07966],
                'compactness_mean': [0.05581],
                'concavity_mean': [0.02087],
                'concave points_mean': [0.02652],
                'symmetry_mean': [0.1589],
                'fractal_dimension_mean': [0.05586],
                # Add more features as needed
            })

            # Preprocess input data
            X_input_scaled = self.scaler.transform(X_input)
            X_input_pca = self.pca.transform(X_input_scaled)

            # Make predictions and get probabilities
            predictions = self.classifier.predict(X_input_pca)
            probabilities = self.classifier.predict_proba(X_input_pca)[:, 1]  # Probability of being malignant

            # Display or use the predictions and probabilities as needed
            result = "The tumor is Malignant (cancerous)" if predictions[0] == 1 else "The tumor is Benign (non-cancerous)"
            confidence = f"Confidence: {probabilities[0] * 100:.2f}%"

            # Display the result and confidence in the GUI (you can use labels, messagebox, etc.)
            print("PREDICTION:", result)
            print(confidence)
        else:
            messagebox.showerror("Error", "Please browse and load a CSV file first.")


if __name__ == "__main__":
    root = tk.Tk()
    app = BreastCancerClassifierApp(root)
    root.mainloop()
