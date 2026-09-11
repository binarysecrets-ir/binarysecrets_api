import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import APIDetail from "./pages/APIDetail";
import './App.css'

export default function App() {
    return (
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/apis/:slug" element={<APIDetail />} />
        </Routes>
    );
}