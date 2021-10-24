import React, { useEffect, useState } from 'react'
import PrevNextNodes from './PrevNextNodes'
import NowNode from './NowNode'

const Nodes = () => {
	const [nodes,     setNodes]		= useState(undefined)
	
	const getPrevNext = (id) => {
		fetch("/get_prev_next/" + id).then(responce => {
			if (responce.ok){
				return responce.json()
            }
        }).then(data => {
			if (typeof data === 'undefined') {
				console.log("Bad get responce")
            }
            else {
				setNodes(data.nodes)
            }
        })
    }

    useEffect(() => {
        getPrevNext(42)
    }, [])

	const handleNodeChange = (id) => {
		getPrevNext(id)
	}

	return (
		<div>
			<div className="container-liquid">
				{
					typeof nodes === 'undefined' ? (
						<div>Loading...</div>
					) : (
						<div className="row">
							<PrevNextNodes nodes={nodes.Prev} onNodeChange={handleNodeChange} />
							<NowNode 	   node ={nodes.Now} />
							<PrevNextNodes nodes={nodes.Next} onNodeChange={handleNodeChange} />
						</div>
					)
				}
			</div>
		</div>
	)
}

export default Nodes
