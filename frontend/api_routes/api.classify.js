import React, {useEffect, useState} from 'react'
import api from '../api/api'

const startDetection = () => {
    // const[data, setData] = useState([])
    // after some voice activation we call this
    // after we click the x button we stop this
    try {
        const response = api.get('/classify')
    } catch (error) {
        console.error("Error fetching", error.message)
    }
}